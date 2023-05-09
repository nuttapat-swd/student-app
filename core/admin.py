from django.contrib import admin

from core import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Address)

