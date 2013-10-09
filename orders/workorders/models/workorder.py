from django.db.models import (BooleanField, CharField, ForeignKey, Model,
    PositiveIntegerField, PositiveSmallIntegerField, TextField)

from orders.models import Order

class WorkOrder(Model):
    order = ForeignKey(Order)
    number = PositiveSmallIntegerField(max_length=3)

    class Meta:
        abstract = True
        app_label = 'workorders'

class PrintWorkOrder(WorkOrder):
    # job_option?
    count_actual = PositiveIntegerField()
    count_reported = PositiveIntegerField(default=0)
    notes = TextField(blank=True)
    impressions = PositiveIntegerField(default=1)
    duplex = BooleanField(default=True)
    weight_oz = PositiveSmallIntegerField(default=1)
    # inserts: many to many with inventory; possibly alter to include only
    #  inserts relevant to the product
    #
    # This should be a reference to the customer model (should be renamed since
    #  there are vendors)
    vendor_print = CharField(max_length=16)

    class Meta:
        app_label = 'workorders'

    @property
    def current_status(self):
        # Do it the same way as Order.
        pass

class PrintMailWorkOrder(PrintWorkOrder):
    # envelopes: inventory
    # Like vendor_print
    vendor_mail = CharField(max_length=16)

    class Meta:
        app_label = 'workorders'
