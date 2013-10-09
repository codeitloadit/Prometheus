from django.db.models import OneToOneField

from addresses.models import Address
from orders.products.models import Product

class GeneralMail(Product):
    return_address = OneToOneField(Address)

    @property
    def name(self):
        return 'General Mail'

    @property
    def work_order_form_classes(self):
        return (('Print and Mail', 'printmailworkorder'),)

    def __str__(self):
        return 'Order <{0!s}> {1}'.format(self.order, self.name)

    def __unicode__(self):
        return unicode(str(self))