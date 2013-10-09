from django.forms import ModelForm

from orders.workorders.models import PrintMailWorkOrder

class PrintMailWorkOrderForm(ModelForm):
    class Meta:
        model = PrintMailWorkOrder

        exclude = 'order',