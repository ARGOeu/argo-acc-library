from .httprequests import HttpRequests
from .installations import Installations, Installation
from .projects import Projects, Project
from .providers import Providers, Provider
from .metrics import (
    InstallationMetric,
    InstallationMetrics,
    ProjectMetric,
    ProjectMetrics,
    ProviderMetrics,
    ProviderMetric,
)
from typing import Optional


class ArgoAccountingService(object):
    """Module main class, to access the REST API"""

    _installations: Optional[Installations] = None
    _projects: Optional[Projects] = None
    _providers: Optional[Providers] = None

    def __init__(self, endpoint, token):
        self._endpoint = endpoint
        self._conn = HttpRequests(token)

    @property
    def installations(self):
        self._installations = self._installations or Installations(self)
        return self._installations

    @property
    def projects(self):
        self._projects = self._projects or Projects(self)
        return self._projects

    @property
    def providers(self):
        self._providers = self._providers or Providers(self)
        return self._providers

    @property
    def connection(self):
        return self._conn

    @property
    def endpoint(self):
        return self._endpoint
