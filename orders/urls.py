from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView

from orders.models.order import Order
from orders.views import OrderDetailView

urlpatterns = patterns('orders.views',
    url(r'(?P<pk>\d*)/detail/?', OrderDetailView.as_view(), name='detail'),

    (r'^(?P<pk>\d*)/workorders/', include('orders.workorders.urls')),
    (r'^$', ListView.as_view(model=Order)))
