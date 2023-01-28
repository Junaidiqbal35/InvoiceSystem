from django import forms

from accounts.models import OrderItems


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = ['item_name', 'quantity']
