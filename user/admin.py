from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
