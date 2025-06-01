from .restresource import RestResourceList, RestResourceItem
from .metrics import ProviderMetrics
from .installations import ProjectProviderInstallations


class Provider(RestResourceItem):
    id = None
    acronym = None
    title = None
    start_date = None
    end_date = None
    call_identifier = None
    providers = None

    def _fetchRoute(self):
        return "provider_entry"

    def _fetchArgs(self):
        return [self.id]

    @property
    def metrics(self):
        return ProviderMetrics(self)


class Providers(RestResourceList):
    def _fetchRoute(self):
        return "provider_list"

    def _fetchArgs(self) -> list:
        return []

    def _createChild(self, data):
        return Provider(self, data)


class ProjectProvider(RestResourceItem):
    def _fetchRoute(self):
        return ""

    def _fetchArgs(self):
        return []

    @property
    def metrics(self):
        return ProviderMetrics(self)

    @property
    def installations(self):
        return ProjectProviderInstallations(self)

class ProjectProviders(RestResourceList):
    def _fetchRoute(self):
        return ""

    def _fetchArgs(self):
        return []

    def __getitem__(self, key: str):
        return ProjectProvider(self, {"id": key})
