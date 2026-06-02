from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ("customer", "status", "created_at")

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = (
            "title",
            "quantity",
            "description",
            "fabric_type",
        )

OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    form=OrderItemForm,
    extra=1,
    can_delete=True,
)
