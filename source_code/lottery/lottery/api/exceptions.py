from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


class APIValidationError(ValidationError):
    pass


class APIObjectNotFound(ValidationError):

    default_code = 'not_found'

    def __init__(self, object_type, object_id):
        message = f'Not found {object_type}({object_id})'
        super(APIObjectNotFound, self).__init__(detail=message)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        data = response.data
        if isinstance(data, dict):
            data = data[list(data.keys())[0]]

        if isinstance(data, list):
            error = data[0]
            response_data = {
                'error': str(error),
                'code': str(error.code)
            }
            response.data = response_data
    return response
