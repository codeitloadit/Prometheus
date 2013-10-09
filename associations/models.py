from django.contrib.localflavor.us.models import PhoneNumberField
from django.db.models import (BooleanField, CharField, ForeignKey, OneToOneField,
    Model)

from accounts.models import Account
from addresses.models import Address
from orders.products import PRODUCT_CHOICES

class Association(Model):
    customer = ForeignKey(Account)
    # I originally wanted to link this to the product model but there's benefit
    # other than preventing from having to know products before runtime and the
    # satisfaction of reusing the model.
    product = CharField(max_length=16, choices=PRODUCT_CHOICES)
    key = CharField(max_length=16)
    name = CharField(max_length=128)
    # office
    phone = PhoneNumberField(blank=True, help_text='Example: 000-000-0000.')
    fax = PhoneNumberField(blank=True, help_text='Example: 000-000-0000.')
    address = OneToOneField(Address, blank=True, null=True)
    remit_address = OneToOneField(Address, blank=True, null=True)
    return_address = OneToOneField(Address, blank=True, null=True)
    approved = BooleanField(default=False)
    archived = BooleanField(default=False)


