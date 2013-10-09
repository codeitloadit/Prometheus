from django.db.models import (CharField, ForeignKey, Model, OneToOneField,
    PositiveSmallIntegerField)

from accounts.models import Account
from associations.models import Association

class StatementAssociationProfile(Model):
    association = OneToOneField(Association)
    management_company_id = CharField(max_length=128, null=True, blank=True)
    bank_id = CharField(max_length=16, null=True, blank=True)
    scanline_setup = CharField(max_length=32, blank=True)
    due_date = CharField(max_length=128, blank=True)
    late_date = CharField(max_length=128, blank=True)
    late_date_message = CharField(max_length=128, blank=True)
    late_amount = CharField(max_length=32, blank=True)
    assessment_frequency = CharField(max_length=128, blank=True, null=True)
    invoice_date = CharField(max_length=128, blank=True)
    topper = CharField(max_length=128, blank=True)
    variable_logo = CharField(max_length=128, blank=True)
    job_option = CharField(max_length=128, blank=True)
    comment = CharField(max_length=128, blank=True)
    # These were in the original model, but don't belong here. These would go in a
    # model under StorageObject.
    # primary_paper_stock = ForeignKey(ColoredStock, blank=True, null=True)
    # secondary_paper_stock = ForeignKey(ColoredStock, blank=True, null=True)
    # nl_modified_date = CharField(max_length=128, blank=True)

class StatementAssociationMessageLine(Model):
    association = ForeignKey(Association)
    number = PositiveSmallIntegerField()
    font = CharField(max_length=1)
    text = CharField(max_length=100)

class StatementGlobalMessageLine(Model):
    customer = ForeignKey(Account)
    number = PositiveSmallIntegerField()
    font = CharField(max_length=1)
    text = CharField(max_length=100)
