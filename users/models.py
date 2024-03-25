from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.IntegerChoices):
        PAINTER = 0, "painter"
        ADMIN = 1, "admin"

    # users role defines what type of API access they will have (only admins
    # can edit and view users)
    role = models.IntegerField(choices=Roles.choices, default=Roles.PAINTER)

    # Users that are owners cannot change their role via the API
    is_owner = models.BooleanField(default=False)
