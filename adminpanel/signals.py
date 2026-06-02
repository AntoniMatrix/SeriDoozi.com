from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from orders.models import Invoice, InvoiceItem, Payment, PaymentStage, PaymentStatus


def create_payments_for_invoice(invoice):
    """پرداخت‌ها رو برای یه فاکتور می‌سازه — فقط یه بار"""
    # اگه قبلاً پرداخت ساخته شده، دوباره نساز
    if Payment.objects.filter(invoice=invoice).exists():
        return

    total_amount = invoice.total
    if total_amount == 0:
        return  # هنوز آیتمی نداره

    currency = invoice.items.first().unit_price_currency if invoice.items.exists() else "IRR"

    if invoice.invoice_type == "MATERIAL":
        Payment.objects.create(
            order=invoice.order,
            invoice=invoice,
            stage=PaymentStage.FULL,
            stage_order=0,
            status=PaymentStatus.PAYABLE,
            amount_currency=currency,
            amount_amount=total_amount,
            description=f"پرداخت خرید پارچه/متریال - پیش‌فاکتور #{invoice.id}",
        )

    elif invoice.invoice_type == "EXECUTION":
        stage_amount = total_amount / 4
        stages = [
            (PaymentStage.CUTTING, "برش", 1),
            (PaymentStage.SEWING, "دوخت", 2),
            (PaymentStage.IRONING, "اتو و بسته‌بندی", 3),
            (PaymentStage.READY, "آماده تحویل", 4),
        ]
        for stage, stage_name, order in stages:
            Payment.objects.create(
                order=invoice.order,
                invoice=invoice,
                stage=stage,
                stage_order=order,
                status=PaymentStatus.INACTIVE,
                amount_currency=currency,
                amount_amount=stage_amount,
                description=f"پرداخت مرحله {stage_name} - پیش‌فاکتور #{invoice.id}",
            )


#@receiver(post_save, sender=InvoiceItem)
#def on_invoice_item_saved(sender, instance, **kwargs):
#    """هر بار که آیتم فاکتور ذخیره شد، سعی کن پرداخت‌ها رو بساز"""
#    create_payments_for_invoice(instance.invoice)
