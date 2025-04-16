from .httprequests import HttpRequests
from .installations import Installations, Installation
from .metrics import Metric, InstallationMetrics


class ArgoAccountingService(object):
    """Module main class, to access the REST API"""

    _installations: Installations | None = None

    def __init__(self, endpoint, token):
        self._endpoint = endpoint
        self._conn = HttpRequests(token)

    @property
    def installations(self):
        self._installations = self._installations or Installations(self)
        return self._installations

    @property
    def connection(self):
        return self._conn

    @property
    def endpoint(self):
        return self._endpoint
