from django.db import models


class WORKER_TYPE(models.IntegerChoices):
    IT = 2, 'IT'
    WORKER = 5, 'Worker'
    CLEANER = 6, 'Cleaner'
    OTHER = 7, 'Other'


class USER_TYPE(models.IntegerChoices):
    ADMIN = 1, 'Admin'
    USER = 2, 'User'
    WORKER = 3, 'Worker'
