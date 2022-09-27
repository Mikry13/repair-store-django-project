from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from users.models import User

BASE_FIELDSETS = (
    (
        'Персональная информация',
        {
            'fields':
                (
                    'first_name',
                    'last_name',
                    'surname',
                    'email',
                    'phone',
                    'position',
                ),
        },
    ),
    (
        'Доступ',
        {
            'fields':
                (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
        },
    ),
    (
        'Основные даты',
        {
            'fields':
                (
                    'last_login',
                    'date_joined',
                ),
        },
    ),
)


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'full_name',
        'phone',
    )
    search_fields = (
        'id',
        'username',
        'last_name',
        'first_name',
        'email',
        'phone',
        'position',
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        *BASE_FIELDSETS,
    )  # type: ignore
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        *BASE_FIELDSETS,
    )
