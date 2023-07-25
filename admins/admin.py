from django.contrib import admin
from .models import Admins, Employee


@admin.register(Admins)
class AdminsAdmin(admin.ModelAdmin):
    None

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    None
