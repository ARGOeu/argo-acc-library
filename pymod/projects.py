from .restresource import RestResourceList, RestResourceItem
from .metrics import ProjectMetrics
from .installations import ProjectInstallations
from .providers import ProjectProviders


class Project(RestResourceItem):
    id = None
    acronym = None
    title = None
    start_date = None
    end_date = None
    call_identifier = None
    _providers = None

    def _fetchRoute(self):
        return "project_entry"

    def _fetchArgs(self):
        return [self.id]

    @property
    def providers(self):
        return ProjectProviders(self)

    @providers.setter
    def providers(self, val):
        self._providers = val

    @property
    def metrics(self):
        return ProjectMetrics(self)

    @property
    def installations(self):
        return ProjectInstallations(self)


class Projects(RestResourceList):
    def _fetchRoute(self):
        return "project_list"

    def _fetchArgs(self) -> list:
        return []

    def _createChild(self, data):
        return Project(self, data)
