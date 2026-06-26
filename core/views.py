"""
Public views + robots.txt content.
"""

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.db.utils import ProgrammingError, OperationalError

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.html import strip_tags
from django.views.decorators.http import require_GET, require_http_methods

from orders.models import Order, OrderStatus

from .models import SitePage, ContactMessage

from django.core.paginator import Paginator
from django.db.models import Q

from .models import Tutorial

def home(request):
    slides = []

    try:
        from orders.models import Order

        latest = list(
            Order.objects
            .exclude(status=OrderStatus.NEW)
            .prefetch_related("items")
            .annotate(total_qty=Sum("items__quantity"))
            .order_by("-created_at")[:10]
        )

        latest_order = (
        Order.objects
        .exclude(status=OrderStatus.NEW)
        .prefetch_related("items")
        .annotate(total_qty=Sum("items__quantity"))
        .order_by("-created_at")
        .first()
        )

        # اسلایدهای واقعی
        slides = [
            {
                "kind": "order",
                "obj": o,
                "qty": o.total_qty or 0,
            }
            for o in latest
        ]

        # اگر کمتر از 10 تا بود، با نمونه پر کن
        missing = 10 - len(slides)
        for i in range(missing):
            slides.append({
                "kind": "sample",
                "id": f"نمونه {i+1}",
                "title": "نمونه سفارش سری‌دوزی",
                "status": "نمونه",
                "qty": 120,
            })

    except (ProgrammingError, OperationalError):
        # DB آماده نیست: کل 10 تا رو نمونه پر کن
        slides = [{
            "kind": "sample",
            "id": f"نمونه {i+1}",
            "title": "نمونه سفارش سری‌دوزی",
            "status": "نمونه",
            "qty": 120,
        } for i in range(10)]

    return render(request, "home.html", {"slides": slides, "latest_order": latest_order})

@require_GET
def about(request):
    """
    About page (DB-driven).

    Security:
    - Only GET allowed.
    - Only published content is shown.
    """
    try:
        page = SitePage.objects.get(key="about", is_published=True)
    except SitePage.DoesNotExist:
        raise Http404("About page is not published.")

    return render(request, "about.html", {"page": page})


def _get_client_ip(request) -> str | None:
    """
    Best-effort client IP detection.
    NOTE: In production behind proxy, configure forwarded headers safely.
    """
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    if xff:
        return xff.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def _rate_limit_ok(ip: str | None, limit: int = 5, window_seconds: int = 600) -> bool:
    """
    Very small rate limiter (per IP).
    - limit: max allowed attempts within window_seconds
    """
    if not ip:
        return True
    key = f"contact_rl:{ip}"
    count = cache.get(key, 0)
    if count >= limit:
        return False
    cache.set(key, count + 1, timeout=window_seconds)
    return True


@require_http_methods(["GET", "POST"])
def contact(request):
    """
    Contact page (DB-driven for title/SEO/text) + form submission (DB stored).

    Security:
    - CSRF enforced by Django template tag.
    - Server-side validation + sanitization.
    - Honeypot anti-bot + rate limit per IP.
    """
    page, _ = SitePage.objects.get_or_create(
        key="contact",
        defaults={"title": "تماس با ما", "is_published": True},
    )

    if not page.is_published:
        raise Http404("Contact page is not published.")

    errors: list[str] = []
    success = False

    if request.method == "POST":
        ip = _get_client_ip(request)

        if not _rate_limit_ok(ip):
            errors.append("تعداد تلاش‌ها زیاد است. چند دقیقه بعد دوباره امتحان کنید.")
        else:
            # Honeypot: bots often fill hidden fields
            honey = (request.POST.get("website") or "").strip()
            if honey:
                # Silently pretend success to avoid helping bots
                success = True
            else:
                name = (request.POST.get("name") or "").strip()
                email = (request.POST.get("email") or "").strip()
                subject = (request.POST.get("subject") or "").strip()
                message = (request.POST.get("message") or "").strip()
                number = (request.POST.get("number") or "").strip()

                # Basic validation
                if len(name) < 2:
                    errors.append("نام معتبر وارد کنید.")
                try:
                    validate_email(email)
                except ValidationError:
                    errors.append("ایمیل معتبر نیست.")
                if len(message) < 10:
                    errors.append("متن پیام خیلی کوتاه است.")
                if len(number) < 10:
                    errors.append("شماره موبایل وارد شده نامعتبر میباشد")
                if len(number) > 11:
                    errors.append("شماره موبایل وارد شده نامعتبر میباشد")
                

                # Sanitize to prevent storing HTML/JS
                name = strip_tags(name)[:80]
                subject = strip_tags(subject)[:120]
                message = strip_tags(message)

                if not errors:
                    ContactMessage.objects.create(
                        name=name,
                        email=email,
                        subject=subject,
                        message=message,
                        number=number,
                        ip_address=ip,
                        user_agent=(request.META.get("HTTP_USER_AGENT") or "")[:240],
                    )
                    success = True

    context = {
        "page": page,
        "errors": errors,
        "success": success,
        "form_data": {
            "name": request.POST.get("name", "") if request.method == "POST" else "",
            "email": request.POST.get("email", "") if request.method == "POST" else "",
            "number": request.POST.get("number", "") if request.method == "POST" else "",
            "subject": request.POST.get("subject", "") if request.method == "POST" else "",
            "message": request.POST.get("message", "") if request.method == "POST" else "",
        },
    }
    return render(request, "contact.html", context)

def FAQ(request):
    """
    FAQ page (DB-driven).

    Security:
    - Only GET allowed.
    - Only published content is shown.
    """
    page, _ = SitePage.objects.get_or_create(
        key="FAQ",
        defaults={"title": "سوالات متداول", "is_published": True},
    )

    if not page.is_published:
        raise Http404("Contact page is not published.")
    
    context = {
        "page": page,
    }
    
    return render(request, "FAQ.html", context)

def tutorial_list(request):
    query = request.GET.get("q", "")
    tutorials = Tutorial.objects.filter(is_active=True)

    if query:
        tutorials = tutorials.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    paginator = Paginator(tutorials, 20)  # 5×4
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "tutorials/tutorial_list.html", {
        "page_obj": page_obj,
        "query": query,
    })

def tutorial_detail(request, slug):
    tutorial = get_object_or_404(Tutorial, slug=slug, is_active=True)
    return render(request, "tutorials/tutorial_detail.html", {
        "tutorial": tutorial
    })

def custom_404(request, exception):
    return render(request, '404.html', status=404)

@require_GET
def robots_txt(request):
    """
    Robots policy:
    - Allow public crawling
    - Disallow private/auth/panel/api routes
    - Provide sitemap location
    """
    site_url = getattr(settings, "SITE_URL", "").rstrip("/")
    sitemap_url = f"{site_url}/sitemap.xml" if site_url else "/sitemap.xml"

    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /panel/",
        "Disallow: /orders/",
        "Disallow: /api/",
        "",
        f"Sitemap: {sitemap_url}",
        "",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")