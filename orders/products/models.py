from django.db.models import Model, OneToOneField

from orders.models import Order

class Product(Model):
    order = OneToOneField(Order, primary_key=True, related_name='product')

    class Meta:
        abstract = True
