from django.contrib.admin import ModelAdmin, site

from models import Order, OrderEvent

class OrderAdmin(ModelAdmin):
    pass

site.register(Order, OrderAdmin)

class OrderEventAdmin(ModelAdmin):
    pass

site.register(OrderEvent, OrderEventAdmin)