import unittest
from .accmocks import InstallationMocks, InstallationMetricMocks, ProjectMocks, ProjectMetricMocks, ProjectProviderMetricMocks
from httmock import urlmatch, HTTMock, response
from pymod import ArgoAccountingService, InstallationMetric
import logging

class TestMetrics(unittest.TestCase):
    def setUp(self):
        self.acc = ArgoAccountingService("localhost", "s3cr3t")
        self.InstallationMocks = InstallationMocks()
        self.InstallationMetricMocks = InstallationMetricMocks()
        self.ProjectMocks = ProjectMocks()
        self.ProjectMetricMocks = ProjectMetricMocks()
        self.ProjectProviderMetricMocks = ProjectProviderMetricMocks()

    def testListTestInstallationMetrics(self):
        """Test the installation metrics listing functionality"""
        with (
            HTTMock(self.InstallationMocks.get_installation_test_mock),
            HTTMock(
                self.InstallationMetricMocks.get_test_installation_metric_list_mock
            ),
        ):
            metrics = self.acc.installations["68179546f1a5b48f0c854353"].metrics
            self.assertEqual(len(list(metrics)), 1)

    def testGetTestInstallationMetricByID(self):
        with HTTMock(
            self.InstallationMetricMocks.get_test_installation_metric_item_mock,
        ):
            metric = self.acc.installations["68179546f1a5b48f0c854353"].metrics[
                "681bc483371ad01d931461bf"
            ]
            self.assertEqual(metric.id, "681bc483371ad01d931461bf")
            self.assertEqual(metric.time_period_start, "2024-01-01T03:43:40Z")
            self.assertEqual(metric.time_period_end, "2024-01-01T09:20:37Z")
            self.assertEqual(metric.value, 66.0336)
            self.assertEqual(metric.user_id, "0123456789abcdef")

    def testGetTestInstallationMetricByIndex(self):
        with HTTMock(
            self.InstallationMetricMocks.get_test_installation_metric_item_mock,
            self.InstallationMetricMocks.get_test_installation_metric_list_mock,
        ):
            metric = self.acc.installations["68179546f1a5b48f0c854353"].metrics[0]
            self.assertEqual(metric.id, "681bc483371ad01d931461bf")
            self.assertEqual(metric.time_period_start, "2024-01-01T03:43:40Z")
            self.assertEqual(metric.time_period_end, "2024-01-01T09:20:37Z")
            self.assertEqual(metric.value, 66.0336)
            self.assertEqual(metric.user_id, "0123456789abcdef")

    def testGetTestInstallationMetricJSON(self):
        with HTTMock(
            self.InstallationMetricMocks.get_test_installation_metric_item_mock,
        ):
            metric = self.acc.installations["68179546f1a5b48f0c854353"].metrics[
                "681bc483371ad01d931461bf"
            ]
            jsons = str(metric)
            self.assertTrue('"id": "681bc483371ad01d931461bf"' in jsons)
            self.assertTrue('"time_period_start": "2024-01-01T03:43:40Z"' in jsons)
            self.assertTrue('"time_period_end": "2024-01-01T09:20:37Z"' in jsons)
            self.assertTrue('"value": 66.0336' in jsons)
            self.assertTrue('"user_id": "0123456789abcdef"' in jsons)

    def testPushInstallationMetricObj(self):
        """
        Test assigning a new metric entry to an installation
        """

        with HTTMock(
            self.InstallationMocks.get_installation_test_mock,
            self.InstallationMetricMocks.get_test_installation_metric_list_mock,
            self.InstallationMetricMocks.post_installation_test_metric_mock,
        ):
            installation = self.acc.installations["68179546f1a5b48f0c854353"]
            m = InstallationMetric(installation.id, {
                "metric_definition_id": "678f89694665a309e8a6c9b2",
                "time_period_start": "2024-01-01T03:43:40Z",
                "time_period_end": "2024-01-01T09:20:37Z",
                "value": 66.0336,
                "group_id": "3f5fc61f3e3af93b",
                "user_id": "9936cb22d3c26a34"
            })
            ret = installation.metrics.add(m)
            self.assertEqual(ret.metric_definition_id, "678f89694665a309e8a6c9b2")
            self.assertEqual(ret.time_period_start, "2024-01-01T03:43:40Z")
            self.assertEqual(ret.time_period_end, "2024-01-01T09:20:37Z")
            self.assertEqual(ret.value, 66.0336)
            self.assertEqual(ret.group_id, "3f5fc61f3e3af93b")
            self.assertEqual(ret.user_id, "9936cb22d3c26a34")

    def testPushInstallationMetricDict(self):
        """
        Test assigning a new metric entry to an installation
        """

        with HTTMock(
            self.InstallationMocks.get_installation_test_mock,
            self.InstallationMetricMocks.get_test_installation_metric_list_mock,
            self.InstallationMetricMocks.post_installation_test_metric_mock,
        ):
            installation = self.acc.installations["68179546f1a5b48f0c854353"]
            m = {
                "metric_definition_id": "678f89694665a309e8a6c9b2",
                "time_period_start": "2024-01-01T03:43:40Z",
                "time_period_end": "2024-01-01T09:20:37Z",
                "value": 66.0336,
                "group_id": "3f5fc61f3e3af93b",
                "user_id": "9936cb22d3c26a34"
            }
            ret = installation.metrics.add(m)
            self.assertEqual(ret.metric_definition_id, "678f89694665a309e8a6c9b2")
            self.assertEqual(ret.time_period_start, "2024-01-01T03:43:40Z")
            self.assertEqual(ret.time_period_end, "2024-01-01T09:20:37Z")
            self.assertEqual(ret.value, 66.0336)
            self.assertEqual(ret.group_id, "3f5fc61f3e3af93b")
            self.assertEqual(ret.user_id, "9936cb22d3c26a34")

    def testPushInstallationMetricStr(self):
        """
        Test assigning a new metric entry to an installation
        """

        with HTTMock(
            self.InstallationMocks.get_installation_test_mock,
            self.InstallationMetricMocks.get_test_installation_metric_list_mock,
            self.InstallationMetricMocks.post_installation_test_metric_mock,
        ):
            installation = self.acc.installations["68179546f1a5b48f0c854353"]
            m = """{"metric_definition_id": "678f89694665a309e8a6c9b2", "time_period_start": "2024-01-01T03:43:40Z", "time_period_end": "2024-01-01T09:20:37Z", "value": 66.0336, "group_id": "3f5fc61f3e3af93b", "user_id": "9936cb22d3c26a34"}"""
            ret = installation.metrics.add(m)
            self.assertEqual(ret.metric_definition_id, "678f89694665a309e8a6c9b2")
            self.assertEqual(ret.time_period_start, "2024-01-01T03:43:40Z")
            self.assertEqual(ret.time_period_end, "2024-01-01T09:20:37Z")
            self.assertEqual(ret.value, 66.0336)
            self.assertEqual(ret.group_id, "3f5fc61f3e3af93b")
            self.assertEqual(ret.user_id, "9936cb22d3c26a34")

    def testListTestProjectMetrics(self):
        """Test the project metrics listing functionality"""
        with (
            HTTMock(self.ProjectMocks.get_project_test_mock),
            HTTMock(
                self.ProjectMetricMocks.get_test_project_metric_list_mock
            ),
        ):
            metrics = self.acc.projects["TESTPROJ01"].metrics
            self.assertEqual(len(list(metrics)), 1)

    def testListTestProjectProviderMetrics(self):
        """Test the project provider metrics listing functionality"""
        with (
            HTTMock(self.ProjectMocks.get_project_test_mock),
            HTTMock(
                self.ProjectProviderMetricMocks.get_test_project_provider_metric_list_mock
            ),
        ):
            metrics = self.acc.projects["TESTPROJ01"].providers["TESTPROV01"].metrics
            self.assertEqual(len(list(metrics)), 1)


if __name__ == "__main__":
    unittest.main()
