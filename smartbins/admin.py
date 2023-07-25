from django.contrib import admin
from .models import Smartbin
# Register your models here.


@admin.register(Smartbin)
class SmartbinAdmin(admin.ModelAdmin):
    None
