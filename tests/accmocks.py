import json

from httmock import response, urlmatch


class ProviderMocks(object):
    LIST_PROVIDERS_RESPONSE = (
        """{"size_of_page":1,"number_of_page":1,"total_elements":1,"total_pages":1,"content":[{"id":"TESTPROV01","""
        """"name":"TEST PROVIDER 01","website":"https://example.org","abbreviation":"TESTPROV01","logo":"""
        """"https://example.org","creator_id":"0123456789abcdef"}], "links": []}"""
    )

    GET_PROVIDER_TEST_RESPONSE = (
        """{"id":"TESTPROV01","name":"TEST PROVIDER 01","website":"https://example.org","abbreviation":"TESTPROV01","""
        """"logo":"https://example.org","creator_id":"0123456789abcdef"}"""
    )

    list_providers_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/providers",
        method="GET",
        query="page=1",
    )

    get_provider_test_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/providers/TESTPROV01",
        method="GET",
    )

    @urlmatch(**list_providers_urlmatch)
    def list_providers_mock(self, url, request):
        assert url.path == "/accounting-system/providers"
        assert request.method == "GET"
        return response(200, self.LIST_PROVIDERS_RESPONSE, None, None, 5, request)

    @urlmatch(**get_provider_test_urlmatch)
    def get_provider_test_mock(self, url, request):
        assert url.path == "/accounting-system/providers/TESTPROV01"
        assert request.method == "GET"
        return response(
            200, self.GET_PROVIDER_TEST_RESPONSE, None, None, 5, request
        )


class ProjectMocks(object):
    LIST_PROJECTS_RESPONSE = (
        """{"size_of_page":1,"number_of_page":1,"total_elements":1,"total_pages":1,"content":[{"id": "TESTPROJ01","""
        """ "acronym": "TestProj01", "title": "TEST PROJECT 01", "start_date": "2024-04-01", "end_date":"""
        """ "2027-03-31", "call_identifier": "TESTCALL01", "providers": [{"id": "TESTPROV01", "name":"""
        """ "Test Provider 01", "website": "https://example.org", "abbreviation": "testprov01", "logo":"""
        """ "https://example.com", "installations": [{"id": "68179546f1a5b48f0c854353", "infrastructure":"""
        """ "TESTINFRA01", "installation": "TESTINSTA01", "resource": "TESTRES01", "unit_of_access": null}]}]}],"""
        """ "links": []}"""
    )

    GET_PROJECT_TEST_RESPONSE = (
        """{"id": "TESTPROJ01", "acronym": "TestProj01", "title": "TEST PROJECT 01", "start_date": "2024-04-01","""
        """ "end_date": "2027-03-31", "call_identifier": "TESTCALL01", "providers": [{"id": "TESTPROV01", "name":"""
        """ "Test Provider 01", "website": "https://example.org", "abbreviation": "testprov01", "logo":"""
        """ "https://example.com", "installations": [{"id": "68179546f1a5b48f0c854353", "infrastructure":"""
        """ "TESTINFRA01", "installation": "TESTINSTA01", "resource": "TESTRES01", "unit_of_access": null}]}]}"""
    )

    list_projects_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/admin/projects",
        method="GET",
        query="page=1",
    )

    get_project_test_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/projects/TESTPROJ01",
        method="GET",
    )

    @urlmatch(**list_projects_urlmatch)
    def list_projects_mock(self, url, request):
        assert url.path == "/accounting-system/admin/projects"
        assert request.method == "GET"
        return response(200, self.LIST_PROJECTS_RESPONSE, None, None, 5, request)

    @urlmatch(**get_project_test_urlmatch)
    def get_project_test_mock(self, url, request):
        assert url.path == "/accounting-system/projects/TESTPROJ01"
        assert request.method == "GET"
        return response(
            200, self.GET_PROJECT_TEST_RESPONSE, None, None, 5, request
        )


class InstallationMocks(object):
    LIST_INSTALLATIONS_RESPONSE1 = (
        """{"size_of_page":10,"number_of_page":1,"total_elements":12,"total_pages":2,"content":["""
        """{"id":"68179546f1a5b48f0c854353","project":"TESTPROJ01","organisation":"TESTORG01","infrastructure":"""
        """"TESTINFRA01","installation":"TESTINSTA01","resource":"TESTRES01","unit_of_access":null},"""
        """{"id":"681795464c2922e4367fe1c4","project":"TESTPROJ02","organisation":"TESTORG02","infrastructure":"""
        """"TESTINFRA02","installation":"TESTINSTA02","resource":"TESTRES02","unit_of_access":null},"""
        """{"id":"681795463c792bf6c23aa741","project":"TESTPROJ03","organisation":"TESTORG03","infrastructure":"""
        """"TESTINFRA03","installation":"TESTINSTA03","resource":"TESTRES03","unit_of_access":null},"""
        """{"id":"681795463ae9de407c8073da","project":"TESTPROJ04","organisation":"TESTORG04","infrastructure":"""
        """"TESTINFRA04","installation":"TESTINSTA04","resource":"TESTRES04","unit_of_access":null},"""
        """{"id":"681795460e9b55f38d982f77","project":"TESTPROJ05","organisation":"TESTORG05","infrastructure":"""
        """"TESTINFRA05","installation":"TESTINSTA05","resource":"TESTRES05","unit_of_access":null},"""
        """{"id":"681795468c189cee4e182e7e","project":"TESTPROJ06","organisation":"TESTORG06","infrastructure":"""
        """"TESTINFRA06","installation":"TESTINSTA06","resource":"TESTRES06","unit_of_access":null},"""
        """{"id":"68179546dce2f040d31e0129","project":"TESTPROJ07","organisation":"TESTORG07","infrastructure":"""
        """"TESTINFRA07","installation":"TESTINSTA07","resource":"TESTRES07","unit_of_access":null},"""
        """{"id":"68179546e21a7a5849d09fb3","project":"TESTPROJ08","organisation":"TESTORG08","infrastructure":"""
        """"TESTINFRA08","installation":"TESTINSTA08","resource":"TESTRES08","unit_of_access":null},"""
        """{"id":"68179546f9116f197e3df2a0","project":"TESTPROJ09","organisation":"TESTORG09","infrastructure":"""
        """"TESTINFRA09","installation":"TESTINSTA09","resource":"TESTRES09","unit_of_access":null},"""
        """{"id":"68179546680552ca72c5c4bb","project":"TESTPROJ10","organisation":"TESTORG10","infrastructure":"""
        """"TESTINFRA10","installation":"TESTINSTA10","resource":"TESTRES10","unit_of_access":null}"""
        """],"links":[]}"""
    )

    LIST_INSTALLATIONS_RESPONSE2 = (
        """{"size_of_page":10,"number_of_page":2,"total_elements":12,"total_pages":2,"content":[{"id":"""
        """"68179546680552ca72c5c4bc","project":"TESTPROJ11","organisation":"TESTORG11","infrastructure":"""
        """"TESTINFRA11","installation":"TESTINSTA11","resource":"TESTRES11","unit_of_access":null},{"id":"""
        """"68179546680552ca72c5c4bd","project":"TESTPROJ12","organisation":"TESTORG12","infrastructure":"""
        """"TESTINFRA12","installation":"TESTINSTA12","resource":"TESTRES12","unit_of_access":null}],"links":[]}"""
    )

    GET_INSTALLATION_TEST_RESPONSE = (
        """{"id": "68179546f1a5b48f0c854353", "project": "TESTPROJ01", "organisation":"""
        """ "TESTORG01", "infrastructure": "TESTINFRA01", "installation": "TESTINSTA01", "resource": "TESTRES01","""
        """ "unit_of_access": null}"""
    )

    list_installations_urlmatch1 = dict(
        netloc="localhost",
        path="/accounting-system/installations/all",
        method="GET",
        query="page=1",
    )

    list_installations_urlmatch2 = dict(
        netloc="localhost",
        path="/accounting-system/installations/all",
        method="GET",
        query="page=2",
    )

    get_installation_test_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/installations/68179546f1a5b48f0c854353",
        method="GET",
    )

    list_test_project_installations_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/projects/TESTPROJ01/installations",
        method="GET",
    )

    list_test_project_providers_installations_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/projects/TESTPROJ01/providers/TESTPROV01/installations",
        method="GET",
        query="page=1",
    )

    @urlmatch(**list_installations_urlmatch1)
    def list_installations_mock1(self, url, request):
        assert url.path == "/accounting-system/installations/all"
        assert request.method == "GET"
        return response(200, self.LIST_INSTALLATIONS_RESPONSE1, None, None, 5, request)

    @urlmatch(**list_installations_urlmatch2)
    def list_installations_mock2(self, url, request):
        assert url.path == "/accounting-system/installations/all"
        assert request.method == "GET"
        return response(200, self.LIST_INSTALLATIONS_RESPONSE2, None, None, 5, request)

    @urlmatch(**get_installation_test_urlmatch)
    def get_installation_test_mock(self, url, request):
        assert url.path == "/accounting-system/installations/68179546f1a5b48f0c854353"
        assert request.method == "GET"
        return response(
            200, self.GET_INSTALLATION_TEST_RESPONSE, None, None, 5, request
        )

    @urlmatch(**list_test_project_installations_urlmatch)
    def get_test_project_installations_mock(self, url, request):
        assert url.path == "/accounting-system/projects/TESTPROJ01/installations"
        assert request.method == "GET"
        return response(200, self.LIST_INSTALLATIONS_RESPONSE1, None, None, 5, request)

    @urlmatch(**list_test_project_providers_installations_urlmatch)
    def get_test_project_provider_installations_mock(self, url, request):
        assert url.path == "/accounting-system/projects/TESTPROJ01/providers/TESTPROV01/installations"
        assert request.method == "GET"
        return response(200, self.LIST_INSTALLATIONS_RESPONSE1, None, None, 5, request)


class InstallationMetricMocks(object):
    LIST_TEST_INSTALLATION_METRIC_LIST_RESPONSE = (
        """{"size_of_page":10,"number_of_page":1,"total_elements":1,"total_pages":1,"content":[
        {"id":"681bc483371ad01d931461bf",
        "time_period_start":"2024-01-01T03:43:40Z",
        "time_period_end":"2024-01-01T09:20:37Z",
        "value":66.0336,
        "project":"TEST PROJECT 01",
        "provider":"TESTPROV01",
        "installation_id":"68179546f1a5b48f0c854353",
        "project_id":"TESTPROJ01",
        "resource":"TESTRES01",
        "user_id":"0123456789abcdef",
        "metric_definition":{
            "metric_definition_id":"678f89694665a309e8a6c9b2",
            "metric_name":"storage",
            "metric_description":"Storage size",
            "unit_type":"TB/year",
            "metric_type":"aggregated",
            "creator_id":"4e0391ea-7b42-4b0a-a1b4-a70dd046df81@example.org"
        }}
    ],"links":[]}"""
    )

    GET_TEST_INSTALLATION_METRIC_RESPONSE = """{
        "metric_id": "681bc483371ad01d931461bf",
        "metric_definition_id": "678f89694665a309e8a6c9b2",
        "time_period_start": "2024-01-01T03:43:40Z",
        "time_period_end": "2024-01-01T09:20:37Z",
        "value": 66.0336,
        "user_id": "0123456789abcdef"
    }"""

    list_test_installation_metrics_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/installations/68179546f1a5b48f0c854353/metrics",
        method="GET",
        query="page=1",
    )

    @urlmatch(**list_test_installation_metrics_urlmatch)
    def get_test_installation_metric_list_mock(self, url, request):
        assert (
            url.path
            == "/accounting-system/installations/68179546f1a5b48f0c854353/metrics"
        )
        assert request.method == "GET"
        return response(
            200,
            self.LIST_TEST_INSTALLATION_METRIC_LIST_RESPONSE,
            None,
            None,
            5,
            request,
        )

    get_test_installation_metric_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/installations/68179546f1a5b48f0c854353/metrics/681bc483371ad01d931461bf",
        method="GET",
    )

    @urlmatch(**get_test_installation_metric_urlmatch)
    def get_test_installation_metric_item_mock(self, url, request):
        assert (
            url.path
            == "/accounting-system/installations/68179546f1a5b48f0c854353/metrics/681bc483371ad01d931461bf"
        )
        assert request.method == "GET"
        return response(
            200,
            self.GET_TEST_INSTALLATION_METRIC_RESPONSE,
            None,
            None,
            5,
            request,
        )

    post_installation_test_metric_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/installations/68179546f1a5b48f0c854353/metrics",
        method="POST",
    )

    @urlmatch(**post_installation_test_metric_urlmatch)
    def post_installation_test_metric_mock(self, url, request):
        assert (
            url.path
            == "/accounting-system/installations/68179546f1a5b48f0c854353/metrics"
        )
        assert request.method == "POST"
        body = json.loads(request.body)
        assert "metric_definition_id" in body
        assert "time_period_start" in body
        assert "time_period_end" in body
        assert "value" in body
        assert "group_id" in body
        assert "user_id" in body
        return response(
            201, body, None, None, 5, request
        )


class ProjectMetricMocks(object):
    LIST_TEST_PROJECT_METRIC_LIST_RESPONSE = (
        """{"size_of_page":10,"number_of_page":1,"total_elements":1,"total_pages":1,"content":[
   {
      "id": "67ed2aaae8af660056233998",
      "time_period_start": "2024-01-01T03:43:40Z",
      "time_period_end": "2024-01-01T09:20:37Z",
      "value": 66.0336,
      "project": "TEST PROJECT 01",
      "provider": "TESTPROV01",
      "installation_id": "68179546f1a5b48f0c854353",
      "project_id": "TESTPROJ01",
      "resource": "TESTRES01",
      "user_id": "0123456789abcdef",
      "metric_definition": {
        "metric_definition_id": "678f89694665a309e8a6c9b2",
        "metric_name": "storage",
        "metric_description": "Storage size",
        "unit_type": "TB/year",
        "metric_type": "aggregated",
        "creator_id": "4e0391ea-7b42-4b0a-a1b4-a70dd046df81@example.org"
      }
    }
    ],"links":[]}"""
    )

    list_test_project_metrics_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/projects/TESTPROJ01/metrics",
        method="GET",
    )

    @urlmatch(**list_test_project_metrics_urlmatch)
    def get_test_project_metric_list_mock(self, url, request):
        assert (
            url.path
            == "/accounting-system/projects/TESTPROJ01/metrics"
        )
        assert request.method == "GET"
        return response(
            200,
            self.LIST_TEST_PROJECT_METRIC_LIST_RESPONSE,
            None,
            None,
            5,
            request,
        )


class ProjectProviderMetricMocks(object):
    LIST_TEST_PROJECT_PROVIDER_METRIC_LIST_RESPONSE = (
        """{"size_of_page":10,"number_of_page":1,"total_elements":1,"total_pages":1,"content":[
   {
      "id": "67ed2aaae8af660056233998",
      "time_period_start": "2024-01-01T03:43:40Z",
      "time_period_end": "2024-01-01T09:20:37Z",
      "value": 66.0336,
      "project": "TEST PROJECT 01",
      "provider": "TESTPROV01",
      "installation_id": "68179546f1a5b48f0c854353",
      "project_id": "TESTPROJ01",
      "resource": "TESTRES01",
      "user_id": "0123456789abcdef",
      "metric_definition": {
        "metric_definition_id": "678f89694665a309e8a6c9b2",
        "metric_name": "storage",
        "metric_description": "Storage size",
        "unit_type": "TB/year",
        "metric_type": "aggregated",
        "creator_id": "4e0391ea-7b42-4b0a-a1b4-a70dd046df81@example.org"
      }
    }
    ],"links":[]}"""
    )

    list_test_project_provider_metrics_urlmatch = dict(
        netloc="localhost",
        path="/accounting-system/projects/TESTPROJ01/providers/TESTPROV01/metrics",
        method="GET",
    )

    @urlmatch(**list_test_project_provider_metrics_urlmatch)
    def get_test_project_provider_metric_list_mock(self, url, request):
        assert (
            url.path
            == "/accounting-system/projects/TESTPROJ01/providers/TESTPROV01/metrics"
        )
        assert request.method == "GET"
        return response(
            200,
            self.LIST_TEST_PROJECT_PROVIDER_METRIC_LIST_RESPONSE,
            None,
            None,
            5,
            request,
        )
