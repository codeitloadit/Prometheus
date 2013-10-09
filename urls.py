from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from orders.products.views import ListProductsView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^test/', 'Prometheus.views.test', name='test'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^orders/new/?$', ListProductsView.as_view(), name='product_selector'),
    url(r'^orders/new/', include('orders.products.urls')),
    url(r'^orders/', include('orders.urls')),)
