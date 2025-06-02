import logging
import os

try:
    from logging import NullHandler
except ImportError:

    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


logger = logging.getLogger(__name__)
if os.getenv("DEBUG") is not None and os.getenv("DEBUG").lower() in [
    "1",
    "t",
    "true",
    "y",
    "yes",
]:
    import sys

    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)
else:
    logger.addHandler(NullHandler())

from .exceptions import (
    AccException,
    AccServiceException,
    AccTimeoutException,
    AccConnectionException,
)
from .argoaccountingservice import (
    ArgoAccountingService,
    Installations,
    Installation,
    InstallationMetrics,
    InstallationMetric,
    Projects,
    Project,
    ProjectMetrics,
    ProjectMetric,
    Providers,
    Provider,
)
