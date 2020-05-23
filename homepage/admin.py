from django.contrib import admin
from .models import CourseMember
from .models import Contribute

# # Register your models here.
admin.site.register(CourseMember)
admin.site.register(Contribute)