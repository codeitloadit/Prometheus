from django.db.models import CharField, Manager, Model

_ACCOUNT_TYPES = (('customer', 'Customer'),
	('optimal', 'Optimal Outsource'),
	('other', 'Other'),
	('vendor', 'Vendor'))

class AccountManager(Manager):
	def customers(self):
		return self.filter(type='customer')

class Account(Model):
	slug = CharField(max_length=16, primary_key=True)
	# management_company_id sucks; very un-descriptive and never relates
	# to the customer name anyway- A2
	name = CharField(max_length=64)
	type = CharField(max_length=8, choices=_ACCOUNT_TYPES, default='customer')

	objects = AccountManager()

	# This is needed to make the models work as a package instead of a module.
	class Meta:
		app_label = 'accounts'
