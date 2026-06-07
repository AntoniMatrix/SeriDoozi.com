"""
Staff panel HTML pages.
Authorization:
- must be staff (group/superuser)
- must have minimum required perms for pages
"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order, OrderStatus, PaymentStatus, Payment, InvoiceItem, Invoice, PaymentStage
from accounts.models import User
from accounts.permissions import is_staff_role, has_perm
from django.contrib import messages
from .signals import create_payments_for_invoice
from django.http import Http404

from django.views.decorators.http import require_http_methods

from core.models import SitePage, ContactMessage
import json


import os
from django.conf import settings
from PIL import Image
import time

from core.models import Tutorial
import jdatetime
from blog.forms import PostAdminForm

stats = {
        "new": Order.objects.filter(status=OrderStatus.NEW).count(),
        "review": Order.objects.filter(status=OrderStatus.REVIEW).count(),
        "quoted": Order.objects.filter(status=OrderStatus.QUOTED).count(),
        "confirmed": Order.objects.filter(status=OrderStatus.CONFIRMED).count(),
        "production": Order.objects.filter(status=OrderStatus.PRODUCTION).count(),
        "ready": Order.objects.filter(status=OrderStatus.READY).count(),
        "delivered": Order.objects.filter(status=OrderStatus.DELIVERED).count(),
    }


@login_required
def dashboard(request):
    """Dashboard page for staff."""
    if not is_staff_role(request.user):
        return HttpResponseForbidden("Forbidden")

    perms = {
        "view_all_orders": has_perm(request.user, "view_all_orders"),
        "change_order_status": has_perm(request.user, "change_order_status"),
        "set_pricing": has_perm(request.user, "set_pricing"),
        "view_financial_reports": has_perm(request.user, "view_financial_reports"),
    }
    return render(request, "adminpanel/dashboard.html", {"stats": stats, "perms": perms})


@login_required
def orders_page(request):
    """Orders list page (requires view_all_orders)."""
    if not is_staff_role(request.user):
        return HttpResponseForbidden("Forbidden")
    if not has_perm(request.user, "view_all_orders"):
        return HttpResponseForbidden("No permission")
    
    orders = Order.objects.order_by("-created_at")

    return render(request, "adminpanel/orders.html", {"stats": stats, "orders": orders})


@login_required
def active_payments(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    
    # بررسی دسترسی (اگر نیاز باشد)
    if not request.user.is_staff and payment.order.customer != request.user:
        return HttpResponseForbidden("شما دسترسی به این پرداخت ندارید")
    
    if payment.stage == PaymentStage.READY:
        return redirect('orders:detail', order_id=payment.order.id)

    payment.status = PaymentStatus.PAYABLE
    payment.save()

    order = get_object_or_404(Order, id=payment.order.pk)
    order.status = OrderStatus.QUOTED
    order.save(update_fields=["status"])
    
    return redirect('orders:detail', order_id=payment.order.id)

@login_required
def cancel_order(request, order_id):
    if request.user.is_staff:
        order = get_object_or_404(Order, id=order_id)
    else:
        order = get_object_or_404(Order, id=order_id, customer=request.user)

    order.payments.exclude(status='PAID').update(status='INACTIVE')
    order.status = OrderStatus.CANCELED
    order.save()

    return redirect('orders:detail', order_id=order.id)
 
@login_required
def create_invoice(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    context = {"stats": stats, "order": order}

    # ── فرم ددلاین ──
    if request.method == "POST" and "save_deadline" in request.POST:
        deadline_shamsi = request.POST.get('deadline')
        if deadline_shamsi:

            year, month, day = map(int, deadline_shamsi.split('/'))
            deadline_miladi = jdatetime.date(year, month, day).togregorian()

            order.deadline = deadline_miladi
            order.save(update_fields=["deadline"])
            messages.success(request, "تاریخ تحویل با موفقیت ذخیره شد.")
        else:
            messages.error(request, "تاریخ تحویل را وارد کنید.")
        return redirect("panel:detail", order_id=order_id)

    # ── فرم فاکتور ──
    if request.method == "POST" and "save_invoice" in request.POST:
        invoice_type = request.POST.get("invoice_type")
        tax_rate = int(request.POST.get("tax_rate", 10))
        total_forms  = int(request.POST.get("items-TOTAL_FORMS", 0))

        if not invoice_type:
            messages.error(request, "نوع فاکتور را انتخاب کنید.")
            return render(request, "adminpanel/create_invoice.html", context)

        # ساخت فاکتور
        invoice = Invoice.objects.create(
            order=order,
            invoice_type=invoice_type,
            tax_rate=tax_rate,
        )

        # ساخت آیتم‌ها
        items_created = 0
        for i in range(total_forms):
            title            = request.POST.get(f"items-{i}-title", "").strip()
            description      = request.POST.get(f"items-{i}-description", "").strip()
            quantity         = int(request.POST.get(f"items-{i}-quantity", 1))
            unit             = request.POST.get(f"items-{i}-unit", "عدد").strip()
            unit_price_amount = int(request.POST.get(f"items-{i}-unit_price_amount", 0))

            if not title:
                continue

            InvoiceItem.objects.create(
                invoice=invoice,
                title=title,
                description=description,
                quantity=quantity,
                unit=unit,
                unit_price_currency="IRR",
                unit_price_amount=unit_price_amount,
            )
            items_created += 1

        create_payments_for_invoice(invoice)

        if items_created == 0:
            invoice.delete()
            messages.error(request, "حداقل یک آیتم معتبر وارد کنید.")
            return render(request, "adminpanel/create_invoice.html", context)

        order = get_object_or_404(Order, id=order_id)
        order.status = OrderStatus.QUOTED
        order.save(update_fields=["status"])

        messages.success(request, f"فاکتور #{invoice.id} با موفقیت ایجاد شد.")
        return redirect("panel:detail", order_id=order_id)

    return render(request, "adminpanel/create_invoice.html", context)

@login_required
def change_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=order_id)
        
        # فقط استاف میتونه تغییر بده
        if not request.user.is_staff:
            messages.error(request, 'شما دسترسی لازم را ندارید.')
            return redirect('panel:detail', order_id=order_id)
        
        new_status = request.POST.get('order_status')
        
        if new_status in ['REVIEW', 'PRODUCTION', 'DELIVERED']:
            order.status = new_status
            order.save(update_fields=['status'])
            messages.success(request, 'وضعیت سفارش با موفقیت تغییر کرد.')
        else:
            messages.error(request, 'وضعیت انتخاب شده معتبر نیست.')
        
        return redirect('panel:detail', order_id=order_id)
    
    return redirect('panel:detail', order_id=order_id)

@login_required
def users(request):
    if not request.user.is_staff:
        raise Http404

    users = User.objects.order_by("date_joined")

    return render(request, "adminpanel/users.html", { 'users' : users, 'stats' : stats })

@login_required
def page_list(request):
    if not request.user.is_staff:
        raise Http404
    pages = SitePage.objects.all().order_by("key")

    return render(request, "adminpanel/page_list.html", {"pages": pages, 'stats' : stats })


@login_required
@require_http_methods(["GET", "POST"])
def page_edit(request, pk):
    if not request.user.is_staff:
        raise Http404
    
    page = get_object_or_404(SitePage, pk=pk)

    if request.method == "POST":
        page.title = request.POST.get("title", "").strip()
        page.meta_title = request.POST.get("meta_title", "").strip()
        page.meta_description = request.POST.get("meta_description", "").strip()
        page.canonical_path = request.POST.get("canonical_path", "").strip()
        page.hero_title = request.POST.get("hero_title", "").strip()
        page.hero_subtitle = request.POST.get("hero_subtitle", "").strip()
        page.body = request.POST.get("body", "").strip()
        page.is_published = request.POST.get("is_published") == "on"

        highlights_raw = request.POST.get("highlights_json", "").strip()
        if highlights_raw:
            try:
                page.highlights_json = json.loads(highlights_raw)
            except json.JSONDecodeError:
                messages.error(request, "فرمت JSON مزیت‌ها نامعتبر است.")
                return render(request, "adminpanel/page_edit.html", {"page": page})
        else:
            page.highlights_json = None

        page.save()
        messages.success(request, "صفحه با موفقیت ذخیره شد.")
        return redirect("panel:page_edit", pk=pk)
    context = {
        "page": page,
        "highlights_display": json.dumps(page.highlights_json, ensure_ascii=False, indent=2) if page.highlights_json else "",
        'stats' : stats 
    }
    return render(request, "adminpanel/page_edit.html", context)


@login_required
def gallery(request):

    if request.method == "POST":
        # مسیر پوشه static/img
        img_dir = os.path.join(settings.BASE_DIR, 'static', 'img')
        
        # تعریف فایل‌ها و فرمت‌های مجاز
        files_config = {
            'LOGO': {'filename': 'LOGO.png', 'format': 'PNG'},
            'hero': {'filename': 'hero.webp', 'format': 'WEBP'},
            'article': {'filename': 'default-article.jpg', 'format': 'JPEG'},
            'OG': {'filename': 'og-default.jpg', 'format': 'JPEG'},
        }
        
        updated = False
        
        for field_name, config in files_config.items():
            uploaded_file = request.FILES.get(field_name)
            
            if uploaded_file:
                try:
                    # باز کردن تصویر با Pillow
                    img = Image.open(uploaded_file)
                    
                    # تبدیل به RGB اگر RGBA باشد (برای JPG)
                    if config['format'] == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
                        img = img.convert('RGB')
                    
                    # مسیر کامل فایل
                    file_path = os.path.join(img_dir, config['filename'])
                    
                    # حذف فایل قبلی اگر وجود داشته باشد
                    if os.path.exists(file_path):
                        os.remove(file_path)
                    
                    # ذخیره فایل جدید
                    img.save(file_path, format=config['format'])
                    updated = True
                    
                except Exception as e:
                    messages.error(request, f'خطا در آپلود {config["filename"]}: {str(e)}')
        
        if updated:
            messages.success(request, 'تصاویر با موفقیت به‌روزرسانی شدند.')
        
        return redirect('panel:gallery')
    
    context = {'ts': int(time.time()), 'stats' : stats }

    return render(request, "adminpanel/gallery.html", context)


@login_required
def tutorial(request):

    if request.method == "POST":
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        thumbnail = request.FILES.get('thumbnail')
        video = request.POST.get('video')
        description = request.POST.get('description', '')
        is_active = request.POST.get('is_active') == 'on'

        try:
            Tutorial.objects.create(
                title=title,
                slug=slug,
                thumbnail=thumbnail,
                video=video,
                description=description,
                is_active=is_active
            )
            messages.success(request, 'آموزش با موفقیت ایجاد شد')
            return redirect('panel:tutorial')
        except Exception as e:
            messages.error(request, f'خطا در ایجاد آموزش: {str(e)}')

    tutorials = Tutorial.objects.all()
    context = {
        'stats': stats,
        'tutorials': tutorials
    }
    return render(request, "adminpanel/create_tutorial.html", context)

@login_required
def contact(request):

    messages = ContactMessage.objects.all().order_by("-created_at")

    return render(request, "adminpanel/contact_list.html", { 'messages' : messages, 'stats' : stats})

@login_required
def contact_detail(request, contact_id):

    if request.method == "POST":
        message = get_object_or_404(ContactMessage, pk=contact_id)
        message.is_read = True
        message.save()
        return redirect('panel:contact_list')


    message = get_object_or_404(ContactMessage, pk=contact_id)

    return render(request, "adminpanel/contact_detail.html", { 'message' : message, 'stats' : stats})

@login_required
def blog(request):

    if request.method == 'POST':
        form = PostAdminForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'پست با موفقیت ایجاد شد')
            return redirect('panel:blog')
    else:
        form = PostAdminForm()


    return render(request, "adminpanel/blog.html", {'stats' : stats, 'form': form})