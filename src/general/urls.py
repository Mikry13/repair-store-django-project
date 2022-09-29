from django.urls import path
from rest_framework.routers import SimpleRouter

from general.api.viewsets import get_database_info

router = SimpleRouter()

urlpatterns = [
    path('db_stats/', get_database_info),
]
