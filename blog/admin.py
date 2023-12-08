from django.contrib import admin
from blog.models import Blogs



@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
