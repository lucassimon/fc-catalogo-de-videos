# Python
from http import HTTPStatus

# Third
from rest_framework import serializers
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from kernel_catalogo_videos.core.exceptions import OperationDBError


class InvalidDataException(APIException, Exception):
    status_code = 422
    default_detail = 'Payload invalid.'

    def __init__(self, operation: str, exc=None, code: int = 500, entity=None, **kwargs) -> None:
        self.code = code or self.status_code
        self.exc = exc
        self.entity = entity
        self.operation = operation
        self.extra = kwargs
        self.message = str(exc) if exc else self.default_detail
        super().__init__(detail=self.message, code=self.code)


class OperationDBErrorAPIException(APIException, OperationDBError):
    status_code = 500
    default_detail = 'Database service internal server error, try again later.'

    def __init__(self, exc, operation: str, code: int = 500, entity=None, **kwargs) -> None:
        self.code = code or self.status_code
        self.exc = exc
        self.entity = entity
        self.operation = operation
        self.extra = kwargs
        self.message = str(exc) or self.default_detail
        super().__init__(detail=self.message, code=self.code)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if hasattr(exc, "code"):
            code = exc.code
        else:

            if hasattr(exc, "status_code"):
                code = exc.status_code
            elif hasattr(response, "status_code"):
                code = response.status_code
            else:
                code = HTTPStatus(500)

        http = HTTPStatus(code)

        if isinstance(exc, serializers.ValidationError):
            data = {
                "code": http,
                "name": http.phrase,
                "description": http.description,
            }

            data.update({"errors": exc.detail})

        else:
            data = {
                "code": http,
                "name": http.phrase,
                "description": http.description,
            }

        if response.data and "detail" in response.data:
            data.update({"detail": response.data.get("detail")})

        if hasattr(exc, "errors"):
            data.update({"errors": exc.get_full_details()})

        if hasattr(exc, "operation"):
            data.update({"operation": exc.operation})

        if hasattr(exc, "message"):
            data.update({"messsage": exc.message or exc.default_detail})

        if hasattr(exc, "__class__"):
            data.update({"exception": exc.__class__.__name__})

        response.data = data

        if hasattr(exc, "entity") and exc.entity is not None:
            response.data["entity"] = exc.entity.to_dict()

        if hasattr(exc, "extra") and exc.extra is not None:
            response.data["extra"] = exc.extra

        response.status_code = http

    return response
