from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import uuid
from django.utils.translation import gettext_lazy as _
from .enum import WORKER_TYPE, USER_TYPE
from .user_manager import CustomUserManager
from django.contrib.auth.hashers import make_password


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now)
    # Make the user active by default.
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        # Means that it is only used by other models, we can't use it directly.
        abstract = True
        ordering = ['created']


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=25, unique=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    role = models.IntegerField(
        choices=USER_TYPE.choices, default=USER_TYPE.USER, db_index=True)

    objects = CustomUserManager()

    # These two functions are essentials for the admin management.
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.role == 1

    @property
    def is_superuser(self):
        return self.role == 1

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, *args, **kwargs):
        if not self.id:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    # Email is the default identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # In default, django uses username, but here we updated it and using email for as an identifier.
    # So we need to tell django that we are using email as an identifier, not the username.

    def get_by_natural_key(self, email):
        return self.__class__.objects.get(email=email)

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name if full_name else self.phone if self.phone else self.email


class Worker(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    worker_type = models.IntegerField(
        choices=WORKER_TYPE.choices, default=WORKER_TYPE.WORKER, db_index=True)
    is_busy = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return f'{self.user}: {self.worker_type}'
