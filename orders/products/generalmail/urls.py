from django.conf.urls.defaults import patterns, url

from orders.products.generalmail.views.submit import Submit

urlpatterns = patterns('orders.products.generalmail.views',
    url(r'^$', Submit.as_view(), name='generalmail-submit'),)

