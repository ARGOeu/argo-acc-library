import unittest
from .accmocks import ProviderMocks
from httmock import HTTMock
from pymod import ArgoAccountingService, Providers


class TestProviders(unittest.TestCase):
    def setUp(self):
        self.acc = ArgoAccountingService("localhost", "s3cr3t")
        self.ProviderMocks = ProviderMocks()

    def testProviderList(self):
        """
        Test the providers listing resource functionality
        """
        with (
            HTTMock(self.ProviderMocks.list_providers_mock),
        ):
            providers = self.acc.providers
            self.assertEqual(len(list(providers)), 1)

    def testGetProviderByID(self):
        """Test fetching a provider by ID"""
        with HTTMock(self.ProviderMocks.get_provider_test_mock):
            provider = self.acc.providers["TESTPROV01"]
            self.assertEqual(provider.id, "TESTPROV01")
            self.assertEqual(provider.name, "TEST PROVIDER 01")
            self.assertEqual(provider.website, "https://example.org")
            self.assertEqual(provider.abbreviation, "TESTPROV01")
            self.assertEqual(provider.logo, "https://example.org")
            self.assertEqual(provider.creator_id, "0123456789abcdef")

    def testGetProviderByIndex(self):
        """
        Test fetching a provider by index
        """
        with HTTMock(self.ProviderMocks.list_providers_mock):
            provider = self.acc.providers[0]
            self.assertEqual(provider.id, "TESTPROV01")
            self.assertEqual(provider.name, "TEST PROVIDER 01")
            self.assertEqual(provider.website, "https://example.org")
            self.assertEqual(provider.abbreviation, "TESTPROV01")
            self.assertEqual(provider.logo, "https://example.org")
            self.assertEqual(provider.creator_id, "0123456789abcdef")

    def testGetTestProviderJson(self):
        """Test JSON representation of an installation"""
        with HTTMock(self.ProviderMocks.get_provider_test_mock):
            provider = self.acc.providers["TESTPROV01"]
            jsons = str(provider)
            self.assertTrue('"id": "TESTPROV01"' in jsons)
            self.assertTrue('"name": "TEST PROVIDER 01"' in jsons)
            self.assertTrue('"website": "https://example.org"' in jsons)
            self.assertTrue('"abbreviation": "TESTPROV01"' in jsons)
            self.assertTrue('"logo": "https://example.org"' in jsons)
            self.assertTrue('"creator_id": "0123456789abcdef"' in jsons)


if __name__ == "__main__":
    unittest.main()
