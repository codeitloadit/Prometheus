from django.conf.urls.defaults import include, patterns, url

from orders.products import product_app_names

# Goal: include the urls provided by each product, i.e., each workflow
# provided by each product.

urlpatterns = []
for name in product_app_names():
    urlpatterns += patterns('orders.products.{0}.views'.format(name),
        url('^{0}/?'.format(name), include('orders.products.{0}.urls'.format(name))))

