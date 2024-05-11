from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(USER)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username","recipename","dietlabel","cuisine","dish","ingredients","health","image")