from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, prodinfo

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/prodinfo', prodinfo, name='prodinfo'),
]