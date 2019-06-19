from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfiles(AbstractBaseUser,PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() # Not yet Created

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """ Retrieve Full Name of user """
        return self.name

    def get_short_name(self):
        """ Does the same thing as above. """
        return self.name

    def __str__(self):
        """ Return string representation of user. """
        """ Not required, but recommended to avoid gibberish. """
        return self.name