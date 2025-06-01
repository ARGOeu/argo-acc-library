from .restresource import RestResourceList, RestResourceItem


class MetricBase(RestResourceItem):
    id = None
    time_period_start = None
    time_period_end = None
    value = None
    project = None
    provider = None
    installation_id = None
    project_id = None
    resource = None
    group_id = None
    user_id = None
    metric_definition_id = None

    def __init__(self, parent, data: dict):
        super().__init__(parent, data)
        if data.get("metric_definition"):
            self.metric_definition = MetricDefinition(self, data["metric_definition"])


class MetricDefinition(RestResourceItem):
    metric_definition_id = None
    metric_name = None
    metric_description = None
    unit_type = None
    metric_type = None
    creator_id = None

    def _fetchRoute(self):
        return ""

    def _fetchArgs(self):
        return []


class Metrics(RestResourceList):
    """Base class for all metrics related subclasses"""

    pass


class InstallationMetric(MetricBase):
    def _fetchRoute(self):
        return "installation_metrics_entry"

    def _fetchArgs(self):
        return [self._parent._parent.id, self.id]


class InstallationMetrics(Metrics):
    def _fetchRoute(self):
        return "installation_metrics_list"

    def _fetchArgs(self):
        return [self._parent.id]

    def _addRoute(self):
        return "installation_metrics_add"

    def _addArgs(self):
        return [self._parent.id]

    def _createChild(self, data):
        return InstallationMetric(self, data)


class ProjectMetric(MetricBase):
    def _fetchRoute(self):
        return ""

    def _fetchArgs(self):
        return []


class ProjectMetrics(Metrics):
    def _fetchRoute(self):
        return "project_metrics_list"

    def _fetchArgs(self):
        return [self._parent.id]

    def _createChild(self, data):
        return ProjectMetric(self, data)


class ProviderMetric(MetricBase):
    def _fetchRoute(self):
        return ""

    def _fetchArgs(self):
        return []


class ProviderMetrics(Metrics):
    def _fetchRoute(self):
        return "project_provider_metric_list"

    def _fetchArgs(self):
        return [self._parent._parent._parent.id, self._parent.id]

    def _createChild(self, data):
        return ProviderMetric(self, data)
