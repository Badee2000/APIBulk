
# Because we are using custom user model using AbstractBaseUser,
# We need to manage the User with a custom user manager.

from django.contrib.auth.models import BaseUserManager
from .enum import USER_TYPE


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # In order to create a super user with admin role we use this function from BaseUserManager.
    def create_superuser(self, email, password=None, **extra_fields):
        # Setting default for admin fields.
        extra_fields.setdefault('role', USER_TYPE.ADMIN)

        return self.create_user(email, password, **extra_fields)
