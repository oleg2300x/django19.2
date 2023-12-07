from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexListView, ProdDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('prodinfo/<int:pk>', ProdDetailView.as_view(), name='prodinfo'),
]