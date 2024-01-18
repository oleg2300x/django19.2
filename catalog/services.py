from config.settings import CACHE_ENABLED
from django.core.cache import cache

from catalog.models import Category


def get_categories_from_cache():
    key = 'category_list'
    if CACHE_ENABLED:
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = Category.objects.all()

        return category_list

