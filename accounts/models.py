"""User model."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import TRDBModel
# Create your models here.


class User(TRDBModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User,  add some extra fields.
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
