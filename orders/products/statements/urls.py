from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('orders.products.statements.views',
    url(r'^$', 'hello', name='statements-submit'),)