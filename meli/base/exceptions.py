class MeliApiException(Exception):
    """
    Generic Exception
    Parameters:
        message: str The error message
        meli_code: str Meli Error Code
        error: list Meli Error list
    """

    code = 999

    def __init__(self, error, headers):
        try:
            self.message = error[0].get("message")
            self.meli_code = error[0].get("code")
        except IndexError:
            pass
        self.error = error
        self.headers = headers


class MeliApiTokenExpired(MeliApiException):
    """
    401	Request has missing or invalid token.
    """

    code = 401

    def __init__(self, error, headers=None):
        super(MeliApiBadRequestException, self).__init__(error, headers)


class MeliApiBadRequestException(MeliApiException):
    """
    400	Request has missing or invalid parameters and cannot be parsed.
    """

    code = 400

    def __init__(self, error, headers=None):
        super(MeliApiBadRequestException, self).__init__(error, headers)


class MeliApiForbiddenException(MeliApiException):
    """
    403	Indicates access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature.
    """

    code = 403

    def __init__(self, error, headers=None):
        super(MeliApiForbiddenException, self).__init__(error, headers)


class MeliApiNotFoundException(MeliApiException):
    """
    404	The resource specified does not exist.
    """

    code = 404

    def __init__(self, error, headers=None):
        super(MeliApiNotFoundException, self).__init__(error, headers)


class MeliApiStateConflictException(MeliApiException):
    """
    409	The resource specified conflicts with the current state.
    """

    code = 409

    def __init__(self, error, headers=None):
        super(MeliApiStateConflictException, self).__init__(error, headers)


class MeliApiTooLargeException(MeliApiException):
    """
    413	The request size exceeded the maximum accepted size.
    """

    code = 413

    def __init__(self, error, headers=None):
        super(MeliApiTooLargeException, self).__init__(error, headers)


class MeliApiUnsupportedFormatException(MeliApiException):
    """
    415	The request payload is in an unsupported format.
    """

    code = 415

    def __init__(self, error, headers=None):
        super(MeliApiUnsupportedFormatException, self).__init__(error, headers)


class MeliApiRequestThrottledException(MeliApiException):
    """
    429	The frequency of requests was greater than allowed.
    """

    code = 429

    def __init__(self, error, headers=None):
        super(MeliApiRequestThrottledException, self).__init__(error, headers)


class MeliApiServerException(MeliApiException):
    """
    500	An unexpected condition occurred that prevented the server from fulfilling the request.
    """

    code = 500

    def __init__(self, error, headers=None):
        super(MeliApiServerException, self).__init__(error, headers)


class MeliApiTemporarilyUnavailableException(MeliApiException):
    """
    503	Temporary overloading or maintenance of the server.
    """

    code = 503

    def __init__(self, error, headers=None):
        super(MeliApiTemporarilyUnavailableException, self).__init__(error, headers)


class MeliApiGatewayTimeoutException(MeliApiException):
    """
    503	Temporary overloading or maintenance of the server.
    """

    code = 504

    def __init__(self, error, headers=None):
        super(MeliApiGatewayTimeoutException, self).__init__(error, headers)


class MissingScopeException(Exception):
    pass


def get_exception_for_code(code: int):
    return {
        400: MeliApiBadRequestException,
        401: MeliApiTokenExpired,
        403: MeliApiForbiddenException,
        404: MeliApiNotFoundException,
        409: MeliApiStateConflictException,
        413: MeliApiTooLargeException,
        415: MeliApiUnsupportedFormatException,
        429: MeliApiRequestThrottledException,
        500: MeliApiServerException,
        503: MeliApiTemporarilyUnavailableException,
        504: MeliApiGatewayTimeoutException,
    }.get(code, MeliApiException)
