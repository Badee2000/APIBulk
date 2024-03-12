from django.db import models
from users.models import BaseModel, User


class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.name}'


class Building(BaseModel):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, db_index=True)
    # Building name MUST be unique.
    # Using UUID make the work harder to get the building by id, so it is more efficient
    # to get the building using its name, making the name unique is preferable in most cases.
    # And it shouldn't be blank in this case.
    name = models.CharField(max_length=255, unique=True)
    floor_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name or "Building"


class Office(BaseModel):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, null=True, db_index=True)
    floor = models.IntegerField(default=0, db_index=True)
    number = models.IntegerField(default=0)

    # There shouldn't be two offices with the same details (different by number in the same floor).
    class Meta:
        unique_together = ['building', 'floor', 'number']

    def __str__(self):
        return f'{self.building} | {self.number}'


class UserOffice(BaseModel):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # It was written `Office` with a capital `O`, Fixed it.
    def __str__(self):
        return f'{self.office}: {self.user}'
