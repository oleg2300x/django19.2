from django.urls import path

from catalog.apps import CatalogConfig
from blog.views import BlogListView, BlogDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('bloginfo/<int:pk>', BlogDetailView.as_view(), name='bloginfo'),
]