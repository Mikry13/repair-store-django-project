from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from users.models import User


class UserAdmin(DefaultUserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'phone',
    )
    search_fields = (
        'id',
        'username',
        'last_name',
        'email',
        'phone',
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'surname', 'email', 'phone', 'avatar', 'position', 'rank')}),
        ('Доступ', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Основные даты', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
