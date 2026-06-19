from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator

User = get_user_model()


# =========================
# Order Status
# =========================
class OrderStatus(TextChoices):
    NEW = "NEW", _("جدید")
    REVIEW = "REVIEW", _("درحال بررسی")
    QUOTED = "QUOTED", _("در انتظار پرداخت")
    CONFIRMED = "CONFIRMED", _("تایید شده")
    PRODUCTION = "PRODUCTION", _("درحال تولید")
    READY = "READY", _("آماده تحویل")
    DELIVERED = "DELIVERED", _("تحویل شده")
    CANCELED = "CANCELED", _("لغو شده")


# =========================
# Size Mode
# =========================
class SizeMode(TextChoices):
    NORMAL = "NORMAL", _("عادی")
    VIP = "VIP", _("VIP")


# =========================
# Order
# =========================
class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="orders",
    )
    title = models.CharField(max_length=255)

    status = models.CharField(
        max_length=12,
        choices=OrderStatus.choices,
        default=OrderStatus.NEW,
    )

    fabric_by_workshop = models.BooleanField(default=False)

    materials_by_workshop = models.BooleanField(default=False)

    stage_num = models.DecimalField(default=0, max_digits=1, decimal_places=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])

    deadline = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self) -> str:
        return f"Order #{self.id} - {self.title}"

    @property
    def total_amount(self):
        """برای سازگاری با کدهای قبلی - از مقدار ذخیره شده استفاده می‌کنه"""
        return self.total_amount_amount

    def calculate_total_amount(self):
        """محاسبه مجموع قیمت آیتم‌ها"""
        return sum(item.total_price for item in self.items.all())
    
    def update_total_amount(self):
        """به‌روزرسانی مبلغ کل"""
        self.total_amount_amount = self.calculate_total_amount()
        self.save(update_fields=['total_amount_amount'])


# =========================
# Order Item
# =========================
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )

    title = models.CharField(
        max_length=200,
        help_text=_("Item title (e.g. Men's Jacket, Pants, Coat)"),
    )

    quantity = models.PositiveIntegerField(default=1)

    description = models.TextField(blank=True)

    # Tailoring specifications
    fabric_type = models.CharField(max_length=100, blank=True)

    # Size info
    size_mode = models.CharField(
        max_length=10,
        choices=SizeMode.choices,
        default=SizeMode.NORMAL,
    )
    size_from = models.CharField(max_length=50, blank=True)
    size_to = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self) -> str:
        return f"{self.quantity} × {self.title}"

    @property
    def total_price(self):
        return self.quantity * self.unit_price_amount


# =========================
# VIP Size Items
# =========================
class OrderItemVipSize(models.Model):
    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        related_name="vip_sizes",
    )
    size = models.CharField(max_length=20)
    quantity = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "VIP Size"
        verbose_name_plural = "VIP Sizes"
        unique_together = ("order_item", "size")

    def __str__(self):
        return f"{self.order_item.title} | {self.size} → {self.quantity}"


# =========================
# Order Files
# =========================
class OrderFile(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="files",
    )
    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="files",
    )
    file = models.FileField(
        upload_to="order_files/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "pdf", "doc", "docx",
                    "jpg", "jpeg", "png",
                    "zip",
                ]
            )
        ],
    )
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Order File")
        verbose_name_plural = _("Order Files")


# =========================
# Order Messages
# =========================
class OrderMessage(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    body = models.TextField()
    is_internal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Order Message")
        verbose_name_plural = _("Order Messages")


# =========================
# Service Type
# =========================
class ServiceType(TextChoices):
    MATERIAL = "MATERIAL", _("خرید پارچه/متریال")
    EXECUTION = "EXECUTION", _("اجرا")


# =========================
# Invoice
# =========================
class Invoice(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="invoices",
    )
    invoice_type = models.CharField(
        max_length=20,
        choices=ServiceType.choices,
    )
    tax_rate = models.DecimalField(
        max_digits=5,
        decimal_places=0,
        default=10,
        help_text=_("Tax rate in percentage (default 10%)"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Invoice #{self.id} - {self.get_invoice_type_display()} for Order #{self.order_id}"

    @property
    def subtotal(self):
        """مجموع قیمت آیتم‌ها بدون مالیات"""
        return sum(item.total_price for item in self.items.all())

    @property
    def tax_amount(self):
        """مبلغ مالیات"""
        return (self.subtotal * self.tax_rate) / 100

    @property
    def total(self):
        """جمع کل با مالیات"""
        return self.subtotal + self.tax_amount


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="items",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        default=1,
    )
    unit = models.CharField(
        max_length=50,
        default="عدد",
        help_text=_("Unit of measurement (e.g. متر, عدد, کیلو)"),
    )
    unit_price_currency = models.CharField(
        max_length=3,
        default="IRR",
    )
    unit_price_amount = models.DecimalField(
        max_digits=12,
        decimal_places=0,
    )

    class Meta:
        verbose_name = _("Invoice Item")
        verbose_name_plural = _("Invoice Items")

    def __str__(self):
        return f"{self.title} - {self.quantity} {self.unit}"

    @property
    def total_price(self):
        """قیمت کل این آیتم"""
        return self.quantity * self.unit_price_amount


# =========================
# Payments
# =========================
class PaymentStatus(TextChoices):
    PAID = "PAID", _("پرداخت شده")
    INACTIVE = "INACTIVE", _("غیر فعال")
    PAYABLE = "PAYABLE", _("قابل پرداخت")


class PaymentStage(TextChoices):
    FULL = "FULL", _("خرج کار و پارچه")  # برای پرداخت متریال
    CUTTING = "CUTTING", _("برش")
    SEWING = "SEWING", _("دوخت")
    IRONING = "IRONING", _("اتو و بسته‌بندی")
    READY = "READY", _("آماده تحویل")


class Payment(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="payments",
    )
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments",
        help_text=_("پیش‌فاکتور مرتبط با این پرداخت"),
    )
    stage = models.CharField(
        max_length=20,
        choices=PaymentStage.choices,
        default=PaymentStage.FULL,
    )
    status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.INACTIVE,
    )
    stage_order = models.IntegerField(
        default=0,
        help_text=_("ترتیب مرحله برای مرتب‌سازی")
    )
    amount_currency = models.CharField(
        max_length=3,
        default="IRR",
    )
    amount_amount = models.DecimalField(
        max_digits=12,
        decimal_places=0,
    )
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    
    # فیلدهای درگاه پرداخت (برای آینده)
    transaction_id = models.CharField(max_length=255,  null=True, blank=True)
    gateway = models.CharField(max_length=50,  null=True, blank=True)

    authority = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        help_text=_("زرین پال authority code for this payment"),
    )

    @property
    def service_type(self):
        """استنتاج نوع سرویس از روی مرحله"""
        return ServiceType.MATERIAL if self.stage == PaymentStage.FULL else ServiceType.EXECUTION

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
        ordering = ["stage_order"]

    def __str__(self):
        return f"Payment {self.amount_amount} {self.amount_currency} - {self.get_status_display()} for Order #{self.order_id}"
