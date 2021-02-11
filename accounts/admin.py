from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """User model admin."""

    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_superuser', 'is_staff', 'created_at', 'updated_at')
