# Might not need to be a separate package but I did it by reflex ahead of time.

from django.views.generic import DetailView

from orders.models import Order

class OrderDetailView(DetailView):
    # This should make the query for the order automatically fetch the product
    # rather than doing a second query
    queryset = Order.objects.select_related('product')

    def get_context_data(self, **kwargs):
        # This should not raise an exception since the base view code will be
        # taking care of it.
        order = kwargs.get('object')
        context = { 'order': order }
        context['work_order_classes'] = order.product.work_order_form_classes

        return context


