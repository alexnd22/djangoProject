from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    is_adult = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
