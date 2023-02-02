from django.utils.translation import gettext
from lottery.api.exceptions import APIValidationError


class UserRefCodeInvalid(APIValidationError):
    default_detail = gettext('Ref code invalid')


class UserEmailExisted(APIValidationError):
    default_detail = gettext('Email already exists')


class VerifiedCodeInvalid(APIValidationError):
    default_detail = gettext('Verified code is not valid')
