import requests
import sys
import logging
import socket
import json

from .exceptions import AccConnectionException, AccServiceException, AccTimeoutException

logger = logging.getLogger(__name__)


class HttpRequests(object):
    """Class for HTTP requests to the Accounting Service API"""

    def __init__(self, token: str):
        self.token = token.rstrip()

        self.routes = {
            "installation_metrics_list": [
                "get",
                "https://{0}/accounting-system/installations/{1}/metrics",
            ],
            "installation_metrics_entry": [
                "get",
                "https://{0}/accounting-system/installations/{1}/metrics/{2}",
            ],
            "installation_list": [
                "get",
                "https://{0}/accounting-system/installations/all",
            ],
            "installation_entry": [
                "get",
                "https://{0}/accounting-system/installations/{1}",
            ],
        }

    def _error_dict(self, response_content, status):
        try:
            error_dict = json.loads(response_content) if response_content else dict()
        except ValueError:
            error_dict = {"error": {"code": status, "message": response_content}}

        return error_dict

    def make_request(
        self, url, route_name, params=None, body=None, **reqkwargs
    ) -> dict:
        """Common method for PUT, GET, POST HTTP requests with appropriate service error handling"""
        m = self.routes[route_name][0]
        decoded = None
        try:
            # the get request based on requests.

            # populate all requests with the Authorization: Bearer token header
            # if there is no defined headers dict in the reqkwargs, introduce it
            if "headers" not in reqkwargs:
                headers = {"authorization": "Bearer {0}".format(self.token)}
                reqkwargs["headers"] = headers
            else:
                # if the there are already other headers defined, just append the x-api-key one
                reqkwargs["headers"]["authorization"] = "Bearer {0}".format(self.token)

            reqmethod = getattr(requests, m)
            logger.debug("doing a " + reqmethod.__name__ + " request on " + url)
            r = reqmethod(url, data=body, params=params, **reqkwargs)

            content = r.content
            status_code = r.status_code

            logger.debug("STATUS CODE:" + str(status_code))
            if status_code == 200:
                decoded = self._error_dict(content, status_code)

            # handle authn/z related errors for all calls
            elif status_code == 401 or status_code == 403:
                raise AccServiceException(
                    json=self._error_dict(
                        content or json.dumps({"message": "Auth failure"}),
                        status_code,
                    ),
                    request=route_name,
                )

            elif status_code == 408:
                raise AccTimeoutException(
                    json=self._error_dict(content, status_code), request=route_name
                )

            # handle any other erroneous behaviour by raising exception
            else:
                raise AccServiceException(
                    json=self._error_dict(content, status_code), request=route_name
                )

        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout,
            socket.error,
        ) as e:
            raise AccConnectionException(e, route_name)

        else:
            return decoded if decoded else {}
