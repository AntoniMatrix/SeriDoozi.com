from django.db import models


class SitePage(models.Model):
    """
    Minimal CMS-like page model for public pages (About/Contact/etc).

    Security note:
    - Keep `body` as plain text for now (render safely in template).
    - If later you need rich HTML, use a safe sanitizer/allowlist editor.
    """

    KEY_CHOICES = (
        ("about", "About"),
        ("contact", "Contact"),
    )

    key = models.CharField(max_length=30, choices=KEY_CHOICES, unique=True)

    title = models.CharField(max_length=120, default="")

    # SEO fields
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    canonical_path = models.CharField(
        max_length=200,
        blank=True,
        help_text="Example: /about/ or /contact/ (leave blank to auto-generate)",
    )

    # Content fields
    hero_title = models.CharField(max_length=120, blank=True)
    hero_subtitle = models.CharField(max_length=240, blank=True)
    body = models.TextField(blank=True)  # plain text

    # Optional flexible content
    highlights_json = models.JSONField(blank=True, null=True)

    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Page"
        verbose_name_plural = "Site Pages"

    def __str__(self) -> str:
        return f"{self.key} - {self.title}"

    def get_canonical_path(self) -> str:
        """
        Return canonical URL path (SEO).
        """
        return self.canonical_path or f"/{self.key}/"


class ContactMessage(models.Model):
    """
    Stores contact form submissions.

    Security:
    - Store minimal metadata for abuse investigation (IP + UA).
    - Do NOT store unnecessary sensitive data.
    """

    name = models.CharField(max_length=80)
    email = models.EmailField()
    number = models.CharField(max_length=11)
    subject = models.CharField(max_length=120, blank=True)
    message = models.TextField()

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=240, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.name} - {self.subject[:30]}"


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="tutorials/thumbnails/")
    video = models.URLField(max_length=500)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
