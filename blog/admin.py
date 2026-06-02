from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import Post
from .forms import PostAdminForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
