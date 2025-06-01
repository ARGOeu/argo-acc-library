import unittest
from .accmocks import InstallationMocks, ProjectMocks, ProviderMocks
from httmock import HTTMock
from pymod import ArgoAccountingService, Installations


class TestInstallations(unittest.TestCase):
    def setUp(self):
        self.acc = ArgoAccountingService("localhost", "s3cr3t")
        self.InstallationMocks = InstallationMocks()
        self.ProjectMocks = ProjectMocks()
        self.ProviderMocks = ProviderMocks()

    def testInstallationsPaging(self):
        """
        Use installations resource as an example to test RestResourceList paging
        functionality, while testing the installations listing resource functionality
        """
        with (
            HTTMock(self.InstallationMocks.list_installations_mock1),
            HTTMock(self.InstallationMocks.list_installations_mock2),
        ):
            installations = self.acc.installations
            self.assertEqual(len(list(installations)), 12)

    def testGetInstallationByID(self):
        """Test fetching an installation by ID"""
        with HTTMock(self.InstallationMocks.get_installation_test_mock):
            installation = self.acc.installations["68179546f1a5b48f0c854353"]
            self.assertEqual(installation.id, "68179546f1a5b48f0c854353")
            self.assertEqual(installation.project, "TESTPROJ01")
            self.assertEqual(installation.organisation, "TESTORG01")
            self.assertEqual(installation.infrastructure, "TESTINFRA01")
            self.assertEqual(installation.installation, "TESTINSTA01")
            self.assertEqual(installation.resource, "TESTRES01")
            self.assertEqual(installation.unit_of_access, None)

    def testGetInstallationByIndex(self):
        """
        Test fetching an installation by index
        Use the 11th (index: 10) entry, to verify indexed results cross pages properly
        """
        with (
            HTTMock(self.InstallationMocks.list_installations_mock1),
            HTTMock(self.InstallationMocks.list_installations_mock2),
        ):
            installation = self.acc.installations[10]
            self.assertEqual(installation.id, "68179546680552ca72c5c4bc")
            self.assertEqual(installation.project, "TESTPROJ11")
            self.assertEqual(installation.organisation, "TESTORG11")
            self.assertEqual(installation.infrastructure, "TESTINFRA11")
            self.assertEqual(installation.installation, "TESTINSTA11")
            self.assertEqual(installation.resource, "TESTRES11")
            self.assertEqual(installation.unit_of_access, None)

    def testGetTestInstallationJson(self):
        """Test JSON representation of an installation"""
        with HTTMock(self.InstallationMocks.get_installation_test_mock):
            installation = self.acc.installations["68179546f1a5b48f0c854353"]
            jsons = str(installation)
            self.assertTrue('"id": "68179546f1a5b48f0c854353"' in jsons)
            self.assertTrue('"project": "TESTPROJ01"' in jsons)
            self.assertTrue('"organisation": "TESTORG01"' in jsons)
            self.assertTrue('"infrastructure": "TESTINFRA01"' in jsons)
            self.assertTrue('"installation": "TESTINSTA01"' in jsons)
            self.assertTrue('"resource": "TESTRES01"' in jsons)
            self.assertTrue('"unit_of_access": null' in jsons)

    def testGetTestProjectInstallationByIndex(self):
        """Test JSON representation of an installation"""
        with (
                HTTMock(self.ProjectMocks.get_project_test_mock),
                HTTMock(self.InstallationMocks.get_test_project_installations_mock)
        ):
            project = self.acc.projects["TESTPROJ01"]
            i = project.installations[0]
            self.assertEqual(i.id, "68179546f1a5b48f0c854353")
            self.assertEqual(i.project, "TESTPROJ01")
            self.assertEqual(i.organisation, "TESTORG01")
            self.assertEqual(i.infrastructure, "TESTINFRA01")
            self.assertEqual(i.installation, "TESTINSTA01")
            self.assertEqual(i.resource, "TESTRES01")
            self.assertEqual(i.unit_of_access, None)

    def testGetTestProjectInstallationJson(self):
        """Test JSON representation of an installation"""
        with (
                HTTMock(self.ProjectMocks.get_project_test_mock),
                HTTMock(self.InstallationMocks.get_test_project_installations_mock)
        ):
            project = self.acc.projects["TESTPROJ01"]
            jsons = str(project.installations[0])
            self.assertTrue('"id": "68179546f1a5b48f0c854353"' in jsons)
            self.assertTrue('"project": "TESTPROJ01"' in jsons)
            self.assertTrue('"organisation": "TESTORG01"' in jsons)
            self.assertTrue('"infrastructure": "TESTINFRA01"' in jsons)
            self.assertTrue('"installation": "TESTINSTA01"' in jsons)
            self.assertTrue('"resource": "TESTRES01"' in jsons)
            self.assertTrue('"unit_of_access": null' in jsons)

    def testGetTestProjectProviderInstallationByIndex(self):
        """Test JSON representation of an installation"""
        with (
                HTTMock(self.InstallationMocks.get_test_project_provider_installations_mock)
        ):
            p = self.acc.projects["TESTPROJ01"].providers["TESTPROV01"]
            i = p.installations[0]
            self.assertEqual(i.id, "68179546f1a5b48f0c854353")
            self.assertEqual(i.project, "TESTPROJ01")
            self.assertEqual(i.organisation, "TESTORG01")
            self.assertEqual(i.infrastructure, "TESTINFRA01")
            self.assertEqual(i.installation, "TESTINSTA01")
            self.assertEqual(i.resource, "TESTRES01")
            self.assertEqual(i.unit_of_access, None)

    def testGetTestProjectProvidersInstallationJson(self):
        """Test JSON representation of an installation"""
        with (
                HTTMock(self.InstallationMocks.get_test_project_provider_installations_mock)
        ):
            p = self.acc.projects["TESTPROJ01"].providers["TESTPROV01"]
            jsons = str(p.installations[0])
            self.assertTrue('"id": "68179546f1a5b48f0c854353"' in jsons)
            self.assertTrue('"project": "TESTPROJ01"' in jsons)
            self.assertTrue('"organisation": "TESTORG01"' in jsons)
            self.assertTrue('"infrastructure": "TESTINFRA01"' in jsons)
            self.assertTrue('"installation": "TESTINSTA01"' in jsons)
            self.assertTrue('"resource": "TESTRES01"' in jsons)
            self.assertTrue('"unit_of_access": null' in jsons)


if __name__ == "__main__":
    unittest.main()
