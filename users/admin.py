from django.contrib import admin
from users.models import User,Feedback


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    None
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    None


# Register your models here.
