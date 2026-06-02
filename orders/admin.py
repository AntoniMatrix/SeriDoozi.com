from django.contrib import admin
from .models import (
    Order, OrderItem, OrderItemVipSize,
    OrderFile, OrderMessage,
    Invoice, InvoiceItem,
    Payment,
)


# =========================
# Inlines
# =========================
class OrderItemVipSizeInline(admin.TabularInline):
    model = OrderItemVipSize
    extra = 0
    fields = ('size', 'quantity')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ('title', 'quantity', 'fabric_type', 'size_mode', 'size_from', 'size_to', 'description')
    show_change_link = True


class OrderFileInline(admin.TabularInline):
    model = OrderFile
    extra = 0
    fields = ('file', 'order_item', 'description', 'uploaded_at')
    readonly_fields = ('uploaded_at',)


class OrderMessageInline(admin.TabularInline):
    model = OrderMessage
    extra = 0
    fields = ('sender', 'body', 'is_internal', 'created_at')
    readonly_fields = ('created_at',)


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0
    fields = ('stage', 'status', 'amount_amount', 'amount_currency', 'stage_order', 'paid_at')
    readonly_fields = ('paid_at',)


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 0
    fields = ('title', 'quantity', 'unit', 'unit_price_amount', 'unit_price_currency')


# =========================
# Order
# =========================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'customer', 'status', 'assigned_to', 'deadline', 'created_at')
    list_filter = ('status', 'fabric_by_workshop', 'materials_by_workshop')
    search_fields = ('title', 'customer__username', 'customer__email')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    inlines = [OrderItemInline, OrderFileInline, OrderMessageInline, PaymentInline]

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'customer', 'status', 'assigned_to')
        }),
        ('تنظیمات', {
            'fields': ('fabric_by_workshop', 'materials_by_workshop', 'deadline')
        }),
        ('تاریخ‌ها', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# =========================
# Order Item
# =========================
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'quantity', 'size_mode', 'fabric_type')
    list_filter = ('size_mode',)
    search_fields = ('title', 'order__title')
    inlines = [OrderItemVipSizeInline]


# =========================
# Invoice
# =========================
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'invoice_type', 'tax_rate', 'created_at')
    list_filter = ('invoice_type',)
    search_fields = ('order__title',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [InvoiceItemInline]

    fieldsets = (
        ('اطلاعات فاکتور', {
            'fields': ('order', 'invoice_type', 'tax_rate')
        }),
        ('تاریخ‌ها', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# =========================
# Payment
# =========================
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'stage', 'status', 'amount_amount', 'amount_currency', 'paid_at')
    list_filter = ('status', 'stage')
    search_fields = ('order__title', 'transaction_id')
    readonly_fields = ('paid_at', 'date')

    fieldsets = (
        ('اطلاعات پرداخت', {
            'fields': ('order', 'invoice', 'stage', 'stage_order', 'status', 'amount_amount', 'amount_currency')
        }),
        ('درگاه پرداخت', {
            'fields': ('transaction_id', 'gateway', 'authority'),
            'classes': ('collapse',)
        }),
        ('تاریخ‌ها', {
            'fields': ('date', 'paid_at', 'description'),
            'classes': ('collapse',)
        }),
    )
