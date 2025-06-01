import unittest
from .accmocks import ProjectMocks
from httmock import HTTMock
from pymod import ArgoAccountingService, Projects


class TestProjects(unittest.TestCase):
    def setUp(self):
        self.acc = ArgoAccountingService("localhost", "s3cr3t")
        self.ProjectMocks = ProjectMocks()

    def testProjectList(self):
        """
        Test the projects listing resource functionality
        """
        with (
            HTTMock(self.ProjectMocks.list_projects_mock),
        ):
            projects = self.acc.projects
            self.assertEqual(len(list(projects)), 1)

    def testGetProjectByID(self):
        """Test fetching a project by ID"""
        with HTTMock(self.ProjectMocks.get_project_test_mock):
            project = self.acc.projects["TESTPROJ01"]
            self.assertEqual(project.id, "TESTPROJ01")
            self.assertEqual(project.acronym, "TestProj01")
            self.assertEqual(project.title, "TEST PROJECT 01")
            self.assertEqual(project.start_date, "2024-04-01")
            self.assertEqual(project.end_date, "2027-03-31")
            self.assertEqual(project.call_identifier, "TESTCALL01")

    def testGetProjectByIndex(self):
        """
        Test fetching a project by index
        """
        with HTTMock(self.ProjectMocks.list_projects_mock):
            project = self.acc.projects[0]
            self.assertEqual(project.id, "TESTPROJ01")
            self.assertEqual(project.acronym, "TestProj01")
            self.assertEqual(project.title, "TEST PROJECT 01")
            self.assertEqual(project.start_date, "2024-04-01")
            self.assertEqual(project.end_date, "2027-03-31")
            self.assertEqual(project.call_identifier, "TESTCALL01")

    def testGetTestProjectJson(self):
        """Test JSON representation of an installation"""
        with HTTMock(self.ProjectMocks.get_project_test_mock):
            project = self.acc.projects["TESTPROJ01"]
            jsons = str(project)
            self.assertTrue('"id": "TESTPROJ01"' in jsons)
            self.assertTrue('"acronym": "TestProj01"' in jsons)
            self.assertTrue('"title": "TEST PROJECT 01"' in jsons)
            self.assertTrue('"start_date": "2024-04-01"' in jsons)
            self.assertTrue('"end_date": "2027-03-31"' in jsons)
            self.assertTrue('"call_identifier": "TESTCALL01"' in jsons)


if __name__ == "__main__":
    unittest.main()
