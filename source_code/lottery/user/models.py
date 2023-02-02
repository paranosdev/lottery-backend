from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'


class User(BaseUser):

    class Meta:
        proxy = True
