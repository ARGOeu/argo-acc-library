import unittest
from .accmocks import InstallationMocks, InstallationMetricMocks
from httmock import urlmatch, HTTMock, response
from pymod import ArgoAccountingService


class TestMetrics(unittest.TestCase):
    def setUp(self):
        self.acc = ArgoAccountingService("localhost", "s3cr3t")
        self.InstallationMocks = InstallationMocks()
        self.InstallationMetricMocks = InstallationMetricMocks()

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


if __name__ == "__main__":
    unittest.main()
