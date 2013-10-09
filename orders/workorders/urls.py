from django.conf.urls.defaults import patterns, url

from views import NewWorkOrderView

urlpatterns = patterns('workorders.views',
    url(r'new/(?P<workorderclass>\w*)/?$', NewWorkOrderView.as_view(), name='newworkorder'))
    # url(r'(?P<pk>\d*)/workorders/?$', ), list work orders, perhaps a quick view or form?

