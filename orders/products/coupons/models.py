from django.contrib.localflavor.us.models import PhoneNumberField
from django.db.models import (CharField, EmailField, ForeignKey, Model, OneToOneField,
    PositiveSmallIntegerField, URLField)

from accounts.models import Account
from addresses.models import Address
from associations.models import Association

class CouponAssociationProfile(Model):
    association = OneToOneField(Association)

class CouponCustomerProfile(Model):
    customer = OneToOneField(Account)
    alt_address = OneToOneField(Address)
    alt_phone = PhoneNumberField(blank=True, help_text='Example: 000-000-0000.')
    alt_fax = PhoneNumberField(blank=True, help_text='Example: 000-000-0000.')
    website = URLField()
    email = EmailField()


class CouponFreeFormMessageLine(Model):
    profile = ForeignKey(CouponCustomerProfile)
    group_number = PositiveSmallIntegerField()
    line_number = PositiveSmallIntegerField()
    text = CharField(max_length=65, blank=True)

class CouponSpecialAssessment(Model):
    pass