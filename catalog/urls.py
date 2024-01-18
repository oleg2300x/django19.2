from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import IndexListView, ProdDetailView, ProdCreateView, ProdUpdateView, ProdDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('prodinfo/<int:pk>', cache_page(60)(ProdDetailView.as_view()), name='prodinfo'),
    path('create/', ProdCreateView.as_view(), name='prod_create'),
    path('update/<int:pk>', ProdUpdateView.as_view(), name='prod_update'),
    path('delete/<int:pk>', ProdDeleteView.as_view(), name='prod_delete'),
]