pipeline {
    agent any
    options {
        checkoutToSubdirectory('argo-acc-library')
    }
    environment {
        PROJECT_DIR="argo-acc-library"
        GIT_COMMIT=sh(script: "cd ${WORKSPACE}/$PROJECT_DIR && git log -1 --format=\"%H\"",returnStdout: true).trim()
        GIT_COMMIT_HASH=sh(script: "cd ${WORKSPACE}/$PROJECT_DIR && git log -1 --format=\"%H\" | cut -c1-7",returnStdout: true).trim()
        GIT_COMMIT_DATE=sh(script: "date -d \"\$(cd ${WORKSPACE}/$PROJECT_DIR && git show -s --format=%ci ${GIT_COMMIT_HASH})\" \"+%Y%m%d%H%M%S\"",returnStdout: true).trim()

    }
    stages {
        stage ('Testing and building...') {
            parallel {              
                stage('Rocky 9') {
                    agent {
                        docker {
                            image 'argo.registry:5000/epel-9-acc'
                            args '-u jenkins:jenkins'
                        }
                    }
                    stages {
                        stage ('Test Rocky 9') {
                            steps {
                                echo 'Executing unit tests @ Rocky 9...'
                                sh '''
                                    cd ${WORKSPACE}/$PROJECT_DIR
                                    rm -f .python-version &>/dev/null
                                    rm -rf .coverage* .tox/ coverage.xml &> /dev/null
                                    source $HOME/pyenv.sh
                                    ALLPYVERS=$(pyenv versions | grep '^[ ]*[0-9]' | tr '\n' ' ')
                                    echo Found Python versions $ALLPYVERS
                                    pyenv local $ALLPYVERS
                                    export TOX_SKIP_ENV="py27.*|py36.*"
                                    tox -p all
                                    coverage xml --omit=*usr* --omit=*.tox*
                                '''
                                cobertura coberturaReportFile: '**/coverage.xml'
                            }
                        }
                        stage ('Build Rocky 9') {
                            steps {
                                echo 'Building Rocky 9 RPM...'
                                withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'jenkins-rpm-repo', usernameVariable: 'REPOUSER', \
                                                                            keyFileVariable: 'REPOKEY')]) {
                                    sh "/home/jenkins/build-rpm.sh -w ${WORKSPACE} -b ${BRANCH_NAME} -d rocky9 -p ${PROJECT_DIR} -s ${REPOKEY}"
                                }
                                archiveArtifacts artifacts: '**/*.rpm', fingerprint: true
                            }
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning workspace and exiting'
            cleanWs()
        }
    }
}

