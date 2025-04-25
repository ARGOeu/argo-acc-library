from .restresource import RestResourceList, RestResourceItem
from .metrics import InstallationMetrics


class Installation(RestResourceItem):
    id = None
    project = None
    organisation = None
    infrastructure = None
    installation = None
    resource = None
    unit_of_access = None

    def _fetchRoute(self):
        return "installation_entry"

    def _fetchArgs(self):
        return [self.id]

    @property
    def metrics(self):
        return InstallationMetrics(self)


class Installations(RestResourceList):
    def _fetchRoute(self):
        return "installation_list"

    def _fetchArgs(self) -> list:
        return []

    def _createChild(self, data):
        return Installation(self, data)
