from django.contrib import admin
from .models import Company, Building, UserOffice, Office

# Register your models here.

admin.site.register(Company)
admin.site.register(Building)
admin.site.register(Office)
admin.site.register(UserOffice)
