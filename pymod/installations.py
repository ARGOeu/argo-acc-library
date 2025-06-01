from .restresource import RestResourceList, RestResourceItem
from .metrics import InstallationMetrics

class InstallationBase(RestResourceItem):
    id = None
    project = None
    organisation = None
    infrastructure = None
    installation = None
    resource = None
    unit_of_access = None

class Installation(InstallationBase):
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


class ProjectInstallation(InstallationBase):
    def _fetchRoute(self):
        return ""

    def _fetchArgs(self):
        return []

    @property
    def metrics(self):
        return InstallationMetrics(self)


class ProjectInstallations(RestResourceList):
    def _fetchRoute(self):
        return "project_installations_list"

    def _fetchArgs(self) -> list:
        return [self._parent.id]

    def _createChild(self, data):
        return ProjectInstallation(self, data)

class ProjectProviderInstallation(InstallationBase):
    def _fetchRoute(self):
        return ""

    def _fetchArgs(self):
        return []

    @property
    def metrics(self):
        return InstallationMetrics(self)


class ProjectProviderInstallations(RestResourceList):
    def _fetchRoute(self):
        return "project_provider_installations_list"

    def _fetchArgs(self) -> list:
        return [self._parent._parent._parent.id, self._parent.id]

    def _createChild(self, data):
        return ProjectProviderInstallation(self, data)
