from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'در صف انتشار'),
        ('published', 'منتشر شد'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    excerpt = models.TextField(
        blank=True,
        help_text='خلاصه کوتاه برای صفحه لیست (حداکثر 160 کاراکتر)'
    )

    thumbnail = models.ImageField(
        upload_to='articles/thumbnails/',
        blank=True,
        null=True
    )

    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    canonical_url = models.URLField(blank=True)

    content = RichTextUploadingField('محتوا')

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    published_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
