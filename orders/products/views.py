from django.views.generic import TemplateView

from orders.products import summary_modules

class ListProductsView(TemplateView):
    template_name = 'orders/products/product_list.html'

    def get_context_data(self, **kwargs):
        return { 'summaries': summary_modules() }
