class AccException(Exception):
    """Base exception class for all Argo Accounting service related errors"""

    def __init__(self, *args, **kwargs):
        super(AccException, self).__init__(*args, **kwargs)


class AccServiceException(AccException):
    """Exception for Argo Accounting Service API errors"""

    def __init__(self, json, request):
        errord = dict()

        if json.get("message"):
            self.msg = "While trying the [{0}]: {1}".format(request, json["message"])
            errord.update(error=self.msg)

        if json.get("code"):
            self.code = json["code"]
            errord.update(status_code=self.code)

        super(AccServiceException, self).__init__(errord)


class AccTimeoutException(AccServiceException):
    """Exception for timeouts errors

    Timeouts can come from the load balancer for partial requests that were not
    completed in the required time frame.
    """

    def __init__(self, json, request):
        super(AccTimeoutException, self).__init__(json, request)


class AccConnectionException(AccException):
    """Exception for connection related problems catched from requests library"""

    def __init__(self, exp, request):
        self.msg = "While trying the [{0}]: {1}".format(request, repr(exp))
        super(AccConnectionException, self).__init__(self.msg)
