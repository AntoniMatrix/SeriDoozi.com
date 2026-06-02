from django.urls import path
from . import views
from orders.views import order_detail_page, order_invoices_list

app_name = "panel"

urlpatterns = [
    path("", views.dashboard, name="panel_dashboard"),
    path("users/", views.users, name="users"),
    path("gallery/", views.gallery, name="gallery"),
    path("tutorial/", views.tutorial, name="tutorial"),
    path("contact/", views.contact, name="contact_list"),
    path("contact/<int:contact_id>/", views.contact_detail, name="contact_detail"),
    path("orders/", views.orders_page, name="panel_orders"),
    path("blog/", views.blog, name="blog"),
    path("orders/<int:order_id>/", order_detail_page, name="detail"),
    path("orders/<int:order_id>/cancel", views.cancel_order, name="cancel"),
    path("pay/<int:payment_id>/", views.active_payments, name="active_pay"),
    path("<int:order_id>/invoice/", views.create_invoice, name="create_invoice"),
    path("orders/<int:order_id>/invoice/", order_invoices_list, name="invoice_list"),
    path("orders/<int:order_id>/status/", views.change_status, name="status"),
    path("sitepage/", views.page_list, name="page_list"),
    path("sitepage/<int:pk>/edit/", views.page_edit, name="page_edit"),
]