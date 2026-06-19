from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, OrderItemFormSet
from .models import Order, OrderStatus, OrderItem, OrderFile, OrderItemVipSize, OrderMessage, Payment, Invoice, InvoiceItem, PaymentStatus, PaymentStage
from django.db import transaction
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
import json
from django.utils import timezone
import os
from django.conf import settings
import requests
from django.urls import reverse
from django.http import Http404
from adminpanel.views import stats


@login_required
def orders_page(request):
    orders = Order.objects.filter(customer=request.user).order_by("-created_at")
    return render(request, "orders/orders.html", {"orders": orders})


@login_required
def order_detail_page(request, order_id):
    # دریافت سفارش همراه با تمام جزئیات مرتبط در یک کوئری
    order = get_object_or_404(
        Order.objects.prefetch_related(
            'items', 
            'items__vip_sizes', 
            'messages', 
            'payments', 
            'files',
            'invoices',
            'customer',
        ), 
        pk=order_id
    )
    
    if order.customer.pk != request.user.id and not request.user.is_staff:
        raise Http404()

    # چک کردن ددلاین
    if order.deadline and order.deadline <= timezone.now().date() and order.status == OrderStatus.PRODUCTION:
        order.status = OrderStatus.QUOTED
        order.save(update_fields=["status"])
        
        # فعال کردن پرداخت آماده تحویل (READY)
        ready_payment = Payment.objects.filter(
            order=order,
            stage=PaymentStage.READY,
            status=PaymentStatus.INACTIVE
        ).first()
    
        if ready_payment:
            ready_payment.status = PaymentStatus.PAYABLE
            ready_payment.save(update_fields=["status"])


    invoice = order.invoices.all()

    total = 0
    for i in invoice:
        total += int(i.total)
    
    context = {
        'order': order,
        'items': order.items.all(),
        'messages': order.messages.all().order_by('-created_at'),
        'payments': order.payments.all().order_by('stage_order'),
        'files': order.files.all(),
        "final_amount": total,
        'payable_payment': order.payments.filter(status='PAYABLE').first(),
        'inactive_payment': order.payments.filter(status='INACTIVE').order_by('stage_order').first(),
        'user': order.customer,
        "stats": stats,
        "orderstatus": OrderStatus,
    }
    
    return render(request, 'orders/order_detail.html', context)


@login_required
@transaction.atomic
def create_order_page(request):

    if request.method == "POST":

        # ✅ ساخت سفارش اصلی
        order = Order.objects.create(
            customer=request.user,
            title=request.POST.get("order_title", ""),
            fabric_by_workshop=bool(request.POST.get("fabric")),
            materials_by_workshop=bool(request.POST.get("material")),
        )

        # ✅ استخراج آیتم‌ها از POST
        items = {}

        for key, value in request.POST.items():
            if key.startswith("items["):
                # مثال:
                # items[0][title]
                # items[0][vip_sizes][1][quantity]

                parts = key.replace("]", "").split("[")
                index = parts[1]
                items.setdefault(index, {})

                # ✅ فیلدهای ساده (NORMAL)
                if len(parts) == 3:
                    items[index][parts[2]] = value

                # ✅ فیلدهای VIP
                elif len(parts) == 5 and parts[2] == "vip_sizes":
                    vip_index = parts[3]
                    vip_field = parts[4]

                    items[index].setdefault("vip_sizes", {})
                    items[index]["vip_sizes"].setdefault(vip_index, {})
                    items[index]["vip_sizes"][vip_index][vip_field] = value

        # ✅ ساخت OrderItemها
        for index, item in items.items():

            size_mode = item.get("size_mode", "NORMAL")

            # =======================
            # ✅ VIP LOGIC (ایزوله)
            # =======================
            if size_mode == "VIP":
                vip_sizes = item.get("vip_sizes", {})

                if not vip_sizes:
                    messages.error(
                        request,
                        "سفارش VIP باید حداقل یک سایز داشته باشد"
                    )
                    return redirect("orders:create")

                total_quantity = 0

                for vip in vip_sizes.values():
                    size = vip.get("size")
                    try:
                        qty = int(vip.get("quantity", 0))
                    except (TypeError, ValueError):
                        qty = 0

                    if not size or qty <= 0:
                        messages.error(
                            request,
                            "اطلاعات سایزهای VIP نامعتبر است"
                        )
                        return redirect("orders:create")

                    total_quantity += qty

                quantity = total_quantity
                size_from = ""
                size_to = ""

            # =======================
            # ✅ NORMAL LOGIC
            # =======================
            else:
                try:
                    quantity = int(item.get("quantity", 1))
                except (TypeError, ValueError):
                    quantity = 1

                size_from = item.get("size_from", "")
                size_to = item.get("size_to", "")

            # ✅ ساخت OrderItem
            order_item = OrderItem.objects.create(
                order=order,
                title=item.get("title", ""),
                description=item.get("description", ""),
                quantity=quantity,
                size_mode=size_mode,
                size_from=size_from,
                size_to=size_to,
                fabric_type=item.get("fabric_type", ""),
            )

            # ✅ ذخیره سایزهای VIP
            if size_mode == "VIP":
                for vip in item.get("vip_sizes", {}).values():
                    OrderItemVipSize.objects.create(
                        order_item=order_item,
                        size=vip.get("size"),
                        quantity=int(vip.get("quantity")),
                    )

            # ✅ فایل نمونه (اختیاری)
            sample_image = request.FILES.get(
                f"items[{index}][sample_image]"
            )

            if sample_image:
                OrderFile.objects.create(
                    order=order,
                    order_item=order_item,
                    file=sample_image,
                    description="Sample image",
                )

        # ✅ پایان موفق
        return redirect("/orders/")

    # ✅ GET
    return render(request, "orders/create_order.html")


@login_required
def send_message(request, order_id):

    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    if request.user.is_staff:
        order = get_object_or_404(Order, id=order_id)
    else:
        order = get_object_or_404(Order, id=order_id, customer=request.user)


    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    text = data.get("message", "").strip()
    if not text:
        return HttpResponseBadRequest("Message is required")

    msg = OrderMessage.objects.create(
        order=order,
        sender=request.user,
        body=text,
    )

    return JsonResponse({
        "status": "success",
        "message_id": msg.id,
    }, status=201)


@login_required
def pay_payment(request, payment_id):
    payment = get_object_or_404(
        Payment,
        pk=payment_id,
        status=PaymentStatus.PAYABLE,
        order__customer=request.user
    )


 # اینجا منطق پرداخت (درگاه یا نقدی) میاد

    amount = int(payment.amount_amount)

    callback_url = request.build_absolute_uri(
        reverse("orders:payment_verify")
    )

    data = {
        "merchant_id": settings.ZARINPAL_MERCHANT_ID,
        "amount": amount,
        "callback_url": callback_url,
        "description": f"Payment for Order #{payment.order_id}"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(
        settings.ZARINPAL_REQUEST_URL,
        json=data,
        headers=headers
    )
    
    print(response)

    result = response.json()

    if response.status_code == 200 and result["data"]["code"] == 100:
        authority = result["data"]["authority"]

        payment.gateway = "zarinpal"
        payment.authority = authority
        payment.save(update_fields=["authority"])

        return redirect(
            f"{settings.ZARINPAL_STARTPAY_URL}{authority}"
        )

    return redirect('orders:detail', order_id=payment.order_id)


@login_required
def payment_verify(request):

    authority = request.GET.get("Authority")
    status = request.GET.get("Status")

    if status != "OK":
        return redirect("orders:list")

    payment = get_object_or_404(
        Payment,
        authority=authority,
        status=PaymentStatus.PAYABLE,
        order__customer=request.user
    )

    data = {
        "merchant_id": settings.ZARINPAL_MERCHANT_ID,
        "amount": int(payment.amount_amount),
        "authority": authority,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(
        settings.ZARINPAL_VERIFY_URL,
        json=data,
        headers=headers
    )



    result = response.json()

    if result["data"]["code"] == 100:
        ref_id = result["data"]["ref_id"]
        
        payment.gateway = "zarinpal"
        payment.transaction_id = ref_id
        payment.status = PaymentStatus.PAID
        payment.paid_at = timezone.now()
        payment.save()

        # فعال‌سازی پرداخت بعدی بر اساس stage_order
        # فعال سازی پرداخت اتوماتیک
        """next_payment = (
            Payment.objects
            .filter(
                order=payment.order,
                stage_order__gt=payment.stage_order,
                status=PaymentStatus.INACTIVE
            )
            .order_by('stage_order')
            .first()
        )

        if next_payment:
            next_payment.status = PaymentStatus.PAYABLE
            next_payment.save()
        """
        
        order = get_object_or_404(Order, id=payment.order_id)

        # اگه پرداخت PAYABLE دیگه‌ای نداره، سفارش CONFIRMED میشه
        has_pending = Payment.objects.filter(
            order=order,
            status=PaymentStatus.PAYABLE,
        ).exists()

        if payment.stage == PaymentStage.READY:
            order.status = OrderStatus.READY
            order.save(update_fields=["status"])
        elif not has_pending and payment.stage != PaymentStage.READY:
            order.status = OrderStatus.CONFIRMED
            order.save(update_fields=["status"])
        else:
            order.status = OrderStatus.QUOTED
            order.save(update_fields=["status"])
        
        match payment.stage:
            case "FULL":
                order.stage_num = 1
            case "CUTTING":
                order.stage_num = 2
            case "SEWING":
                order.stage_num = 3
            case "IRONING":
                order.stage_num = 4
            case "READY":
                order.stage_num = 5

        order.save(update_fields=["stage_num"])

        return redirect('orders:detail', order_id=payment.order_id)

    return redirect('orders:detail', order_id=payment.order_id)


@login_required
def order_invoices_list(request, order_id):
    """لیست فاکتورهای یک سفارش — وقتی چند فاکتور وجود داره"""
    
    if request.user.is_staff:
        order = get_object_or_404(Order, id=order_id)
    else:
        order = get_object_or_404(Order, id=order_id, customer=request.user)
        
    invoices = Invoice.objects.filter(order=order).order_by("created_at")
    return render(request, "orders/invoices_list.html", {
        "order": order,
        "invoices": invoices,
    })


@login_required
def order_invoice_pdf(request, order_id, invoice_id):
    order = get_object_or_404(
        Order.objects.prefetch_related("items", "payments"),
        id=order_id,
        customer=request.user,
    )
    invoice = get_object_or_404(
        Invoice.objects.prefetch_related("items"),
        id=invoice_id,
        order=order,
    )

    paid_amount = sum(p.amount_amount for p in invoice.payments.filter(status='PAID'))

    context = {
        "order": order,
        "invoice": invoice,
        "tax_rate": invoice.tax_rate,
        "tax_amount": invoice.tax_amount,
        "subtotal": invoice.subtotal,
        "final_amount": invoice.total,
        "paid_amount": paid_amount,
        "remaining": invoice.total - paid_amount,
        "site_name": os.environ.get("SITE_NAME", "کارگاه"),
        "business_phone": os.environ.get("BUSINESS_PHONE", ""),
        "business_email": os.environ.get("BUSINESS_EMAIL", ""),
        "business_address": ", ".join(filter(None, [
            os.environ.get("BUSINESS_REGION", ""),
            os.environ.get("BUSINESS_CITY", ""),
            os.environ.get("BUSINESS_STREET", ""),
        ])),
    }

    return render(request, "orders/invoice_pdf.html", context)

