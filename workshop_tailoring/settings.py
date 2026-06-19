"""
Global Django settings.

Goals:
- Clean project structure (GitHub-ready)
- Security hardening for production
- SEO defaults injected via context processor
- MySQL database
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# ----------------------------
# Core
# ----------------------------
SECRET_KEY = "e(df#yn$beiv_0dz^rr(@h*%x)82!4d&um_#m(5c88q0+qeez2"
DEBUG = os.environ.get("DEBUG") == "True"

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1"
).split(",")
    
# ----------------------------
# Apps
# ----------------------------
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    'django.contrib.humanize',
    'ckeditor',
    'ckeditor_uploader',
    'jalali_date',
    # Third-party
    "csp",

    # Local
    "core",
    "accounts",
    "orders",
    "adminpanel",
    "blog"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Whitenoise serves static files in production without extra setup
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",

    # CSRF protection
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Content Security Policy (CSP) - mitigates XSS
    "csp.middleware.CSPMiddleware",

    'adminpanel.middleware.StaffOnlyPanelMiddleware',
]

ROOT_URLCONF = "workshop_tailoring.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # SEO defaults available in all templates
                "core.context_processors.seo_defaults",
            ],
        },
    }
]

WSGI_APPLICATION = "workshop_tailoring.wsgi.application"
ASGI_APPLICATION = "workshop_tailoring.asgi.application"

# ----------------------------
# Database (MySQL)
# ----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

# ----------------------------
# Auth
# ----------------------------
AUTH_USER_MODEL = "accounts.User"
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------
# I18N
# ----------------------------
LANGUAGE_CODE = "fa-IR"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

# ----------------------------
# Static/Media
# ----------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static",]
STATIC_ROOT = BASE_DIR / "staticfiles"


# Use compressed manifest storage for better caching in production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

WHITENOISE_MAX_AGE = 2592000

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'allowedContent': True,
        'extraAllowedContent': 'iframe[*]',
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
        'removePlugins': 'exportpdf',  # ✅ غیرفعال کردن exportpdf
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'extraPlugins': ','.join([
            'uploadimage',
            'image2',
        ]),
        'uploadUrl': '/ckeditor/upload/',
    },
}

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False


MEDIA_URL = "/media/"
MEDIA_ROOT = "/home/seridoozicom/public_html/media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------
# Security (Production-ready defaults)
# ----------------------------
# NOTE: Some settings depend on HTTPS. Enable them when deploying with TLS.

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # must be readable by JS if you use Fetch with CSRF cookie
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

SECURE_BROWSER_XSS_FILTER = True  # old header, still ok
X_FRAME_OPTIONS = "DENY"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = "same-origin"
# SSL

SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# Only set secure cookies when HTTPS is enabled
SESSION_COOKIE_SECURE = not DEBUG and SECURE_SSL_REDIRECT
CSRF_COOKIE_SECURE = not DEBUG and SECURE_SSL_REDIRECT

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# HSTS should be enabled only when you are 100% on HTTPS
SECURE_HSTS_SECONDS = 31536000 if (not DEBUG and SECURE_SSL_REDIRECT) else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG and SECURE_SSL_REDIRECT
SECURE_HSTS_PRELOAD = not DEBUG and SECURE_SSL_REDIRECT

# If behind a reverse proxy that sets X-Forwarded-Proto:
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ----------------------------
# CSP (Content Security Policy)
# ----------------------------
# Keep CSP strict; allow only self. If you add external scripts/fonts, whitelist them explicitly.
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ("'self'",),

        # ✅ اضافه کردن 'unsafe-inline' و 'unsafe-eval' برای CKEditor
        "script-src": (
            "'self'", 
            "'unsafe-inline'",  # برای inline scripts CKEditor
            "'unsafe-eval'",    # برای eval در CKEditor
            "https://cdn.jsdelivr.net",
            "https://aparat.com",
            "https://*.aparat.com",
            "https://zarinpal.com",
            "https://*.zarinpal.com",
            "https://enamad.ir/",
            "https://*.enamad.ir/",
        ),

        "style-src": (
            "'self'", 
            "'unsafe-inline'", 
            "https://cdn.jsdelivr.net",
            "https://aparat.com",
            "https://*.aparat.com",
            "https://zarinpal.com",
            "https://*.zarinpal.com",
            "https://enamad.ir/",
            "https://*.enamad.ir/",
        ),

        # ✅ اضافه کردن blob: برای preview تصاویر در CKEditor
        "img-src": (
            "'self'",
            "data:",
            "blob:",  # برای CKEditor image preview
            "https://cdn.jsdelivr.net",
            "https://neshan.org",
            "https://*.neshan.org",
            "https://aparat.com",
            "https://*.aparat.com",
            "https://zarinpal.com",
            "https://*.zarinpal.com",
            "https://enamad.ir/",
            "https://*.enamad.ir/",
        ),

        "media-src": (
            "'self'",
            "blob:",
            "data:",
            "https://cdn.jsdelivr.net",
            "https://aparat.com",
            "https://*.aparat.com",
        ),

        "font-src": ("'self'", "data:", "https://cdn.jsdelivr.net"),

        "connect-src": ("'self'", "https://cdn.jsdelivr.net"),

        "frame-ancestors": ("'none'",),

        "frame-src": (
            "'self'", 
            "https://neshan.org", 
            "https://*.neshan.org",
            "https://aparat.com",
            "https://*.aparat.com",
            "https://zarinpal.com",
            "https://*.zarinpal.com",
            "https://enamad.ir/",
            "https://*.enamad.ir/",
        ),

        "base-uri": ("'self'",),
        "object-src": ("'none'",),
        "form-action": ("'self'",),
    }
}

# ----------------------------
# SEO / Site config (editable)
# ----------------------------

SITE_NAME = "کارگاه سری‌دوزی"
SITE_URL = os.environ.get("SITE_URL")
SITE_DEFAULT_DESCRIPTION = "ثبت سفارش سری‌دوزی، دریافت پیش‌فاکتور، پیگیری تولید و مدیریت سفارش‌های کارگاه."
SITE_DEFAULT_OG_IMAGE = os.environ.get("SITE_DEFAULT_OG_IMAGE")

BUSINESS = {
    "name": SITE_NAME,
    "type": "LocalBusiness",
    "telephone": os.environ.get("BUSINESS_PHONE"),
    "email": os.environ.get("BUSINESS_EMAIL"),
    "address": {
        "streetAddress": "تهرانپارس بلوار پروین خیابان 196شرقی خیابان 133جنوبی پلاک127",
        "addressLocality": "تهران",
        "addressRegion": "تهران",
        "postalCode": os.environ.get("BUSINESS_POSTAL"),
        "addressCountry": os.environ.get("BUSINESS_COUNTRY"),
    },
    "mapEmbedURL": os.environ.get("BUSINESS_MAP_EMBED_URL"),
    "WHATSAPP_URL": os.environ.get("BUSINESS_WHATSAPP_URL"),
    "TELEGRAM_URL": os.environ.get("BUSINESS_TELEGRAM_URL"),
    "INSTAGRAM_URL": os.environ.get("BUSINESS_INSTAGRAM_URL"),
    "sameAs": [],
}

# ----------------------------
# Logging (basic but useful)
# ----------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}

ZARINPAL_MERCHANT_ID = os.environ.get("ZARINPAL_MERCHANT_ID")

ZARINPAL_SANDBOX = os.environ.get("ZARINPAL_SANDBOX") == "True"

if ZARINPAL_SANDBOX:
    ZARINPAL_REQUEST_URL = os.environ.get("ZARINPAL_REQUEST_URL_SANDBOX")
    ZARINPAL_VERIFY_URL = os.environ.get("ZARINPAL_VERIFY_URL_SANDBOX")
    ZARINPAL_STARTPAY_URL = os.environ.get("ZARINPAL_STARTPAY_URL_SANDBOX")
else:
    ZARINPAL_REQUEST_URL = os.environ.get("ZARINPAL_REQUEST_URL")
    ZARINPAL_VERIFY_URL = os.environ.get("ZARINPAL_VERIFY_URL")
    ZARINPAL_STARTPAY_URL = os.environ.get("ZARINPAL_STARTPAY_URL")

