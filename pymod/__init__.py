import logging
import os

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logger = logging.getLogger(__name__)
if os.getenv("DEBUG"):
    import sys
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)
else:
    logger.addHandler(NullHandler())

from .exceptions import AccException, AccServiceException, AccTimeoutException, AccConnectionException
from .argoaccountingservice import ArgoAccountingService, Metric, Installations, Installation, InstallationMetrics
