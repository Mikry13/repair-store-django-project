from django.contrib import admin
from django.urls import path

from general.api.viewsets import get_database_info


class MyAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('stats/', self.admin_view(get_database_info), name='stats'),
        ]
        return my_urls + urls

    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request)
        app_list += [
            {
                "name": 'Статистика записей в базе данных',
                "app_label": "my_test_app",
                "app_url": "stats",
                "models": [
                ],
            },
        ]
        return app_list


admin_site = MyAdminSite()
