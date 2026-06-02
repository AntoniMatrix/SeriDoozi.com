from django.contrib import admin
from .models import SitePage, ContactMessage, Tutorial


@admin.register(SitePage)
class SitePageAdmin(admin.ModelAdmin):
    list_display = ("key", "title", "is_published", "updated_at")
    list_filter = ("key", "is_published")
    search_fields = ("title", "meta_title", "meta_description")
    readonly_fields = ("updated_at",)
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('key', 'title', 'is_published')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'canonical_path'),
            'classes': ('collapse',)
        }),
        ('محتوا', {
            'fields': ('hero_title', 'hero_subtitle', 'body', 'highlights_json')
        }),
        ('تاریخ‌ها', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "email", "subject", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at", "ip_address", "user_agent")
    list_editable = ("is_read",)
    date_hierarchy = "created_at"
    
    fieldsets = (
        ('اطلاعات تماس', {
            'fields': ('name', 'email', 'number', 'subject', 'message', 'is_read')
        }),
        ('متادیتا', {
            'fields': ('ip_address', 'user_agent', 'created_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    list_editable = ("is_active",)
    date_hierarchy = "created_at"
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'is_active')
        }),
        ('محتوا', {
            'fields': ('thumbnail', 'video', 'description')
        }),
        ('تاریخ‌ها', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
