from random import randint

from django.db.models import (CharField, DateField, EmailField, ForeignKey,
    permalink, PositiveIntegerField, TextField)

from accounts.models import Account
from mixins import ModifiedMixin

class Order(ModifiedMixin):
    order_id = CharField(max_length=12, primary_key=True, blank=False)
    customer = ForeignKey(Account)

    job_name = CharField(max_length=120)
    purchase_order = CharField(max_length=30, blank=True)

    special_instructions = TextField(blank=True)

    alt_contact_name = CharField(max_length=120, blank=True)
    alt_contact_email = EmailField(blank=True)

    expected_count = PositiveIntegerField(default=0)
    due_date = DateField(blank=True, null=True)

    # This is needed to make the models work as a package instead of a module.
    class Meta:
        app_label = 'orders'

    @property
    def current_status(self):
        return self.public_events.latest()

    @property
    def is_rush(self):
        # submitted_event = self.events.get(submitted)
        # return self.due_date - submitted_event.created_date <= C
        pass

    @property
    def public_events(self):
        # I don't like orders having to know about the event internals. Clean this up if possible.
        return self.events.exclude(ordinal=-1)

    @permalink
    def get_absolute_url(self):
        return ('detail', [self.order_id] )

    def next_order_id(self):
        # TODO: this is not how we should generate IDs in production.
        return str(randint(0, 999999999999))

    def save(self, *args, **kwargs):
        # Overridden to make sure that the order ID is never empty.
        if self.order_id == '':
            self.order_id = self.next_order_id()

        super(Order, self).save(*args, **kwargs)
