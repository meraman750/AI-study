from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)

    is_verified = models.BooleanField(default=False)

    bio = models.TextField(blank=True, null=True)

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username