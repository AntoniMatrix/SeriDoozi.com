from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = "مدیریت سفارش‌ها"
    
    def ready(self):
        import adminpanel.signals  # ثبت سیگنال‌ها
