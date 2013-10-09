from django.db.models import Model, CharField

# Create your models here.
class Address(Model):
	recepient_1 = CharField(max_length=64)
	recepient_2 = CharField(max_length=64)

	delivery_point_1 = CharField(max_length=64)
	delivery_point_2 = CharField(max_length=64)

	last_line = CharField(max_length=64)

	@property
	def city_state_zip(self):
		words = self.last_line.split()
		if len(words) >= 3:
			zip = words[-1]
			state = words[-2]
			city = words[:-3]

			return city, state, zip

		return self.last_line, None, None

	@property
	def is_empty(self):
		count = 0
		for field in (self._meta.fields):
			if getattr(self, field.name):
				count += 1

		return count <= 0

	@classmethod
	def from_multiline_string(cls, s):
		'''
		Creates an Address from a multiline string, if possible. If not,
		an empty Address is returned.
		'''
		result = Address()
		lines = s.splitlines()
		count = len(lines)
		if count >= 3 and count <= 5:
			result.recepient_1 = lines[0]
			result.last_line = lines[-1]
			if count == 3:
				result.delivery_point_1 = lines[1]
			elif count == 4:
				# This case is ambiguous. Choosing to use the delivery point,
				# arbitrarily.
				result.delivery_point_1 = lines[1]
				result.delivery_point_2 = lines[2]
			elif count == 5:
				result.recepient_2 = lines[1]
				result.delivery_point_1 = lines[2]
				result.delivery_point_2 = lines[3]

		return result