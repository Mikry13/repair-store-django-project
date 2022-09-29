from django.contrib.admin import apps


class MyAdminConfig(apps.AdminConfig):
    default_site = 'general.admin.MyAdminSite'
