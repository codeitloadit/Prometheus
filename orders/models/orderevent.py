from django.db.models import ForeignKey, Manager, PositiveSmallIntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver

from events.mixins import ReferenceEvent, WorkflowCompareMixin
from events.models import Event
from orders.models import Order

# If all goes well, we don't need Open anymore!
#Open = ReferenceEvent(1)
Reopened = ReferenceEvent('Reopened', 1)
Submitted = ReferenceEvent('Submitted', 2)
Proofed = ReferenceEvent('Proofed', 3)
Approved = ReferenceEvent('Approved', 4)
InProduction = ReferenceEvent('In Production', 5)
OnTime = ReferenceEvent('On-Time', 6)
Billing = ReferenceEvent('Billing', 7)
Complete = ReferenceEvent('Complete', 8)
Closed = ReferenceEvent('Closed', 9)
# Incomparable is how we will identify internal events.
Incomparable = ReferenceEvent('<Nameless Event>', -1)

class OrderEventManager(Manager):
    def from_reference(self, o):
        return OrderEvent(ordinal=o.ordinal, name=o.name)

class OrderEvent(Event, WorkflowCompareMixin):
    order = ForeignKey(Order, related_name='events')
    # As required by WorkflowCompareMixin.
    ordinal = PositiveSmallIntegerField(default=2)

    objects = OrderEventManager()

    # This is needed to make the models work as a package instead of a module.
    class Meta:
        app_label = 'orders'
        get_latest_by = 'created_date'
        ordering = ('-created_date',)

    @property
    def is_internal(self):
        return self.ordinal == Incomparable.ordinal

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(str(self.name))

@receiver(post_save, sender=Order)
def created_event(sender, **kwargs):
    if kwargs.get('created', False):
        instance = kwargs.get('instance')
        e = OrderEvent.objects.from_reference(Submitted)
        e.message = 'New order submitted.'
        e.order = instance
        e.created_by = instance.created_by
        e.save()
