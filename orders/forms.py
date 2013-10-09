from django.forms import ModelForm

from orders.models import Order

class NewOrderForm(ModelForm):
    # Any new order uses this form regardless of product.
    class Meta:
        model = Order
        exclude = ('order_id', 'customer', 'due_date', 'created_by', 'modified_by')


