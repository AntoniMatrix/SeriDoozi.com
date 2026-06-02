from django.urls import path
from . import views
from .views import create_order_page

app_name = "orders"

urlpatterns = [
    path("", views.orders_page, name="list"),
    path("<int:order_id>/", views.order_detail_page, name="detail"),
    path("<int:order_id>/message/", views.send_message, name="send_message"),
    path("create/", create_order_page, name="create"),
    path('pay/<int:payment_id>/', views.pay_payment, name='pay'),
    path("payments/verify/", views.payment_verify, name="payment_verify"),
    path("<int:order_id>/invoice/", views.order_invoices_list, name="invoice_list"),
    path("<int:order_id>/invoice/<int:invoice_id>/", views.order_invoice_pdf, name="invoice"),
]
