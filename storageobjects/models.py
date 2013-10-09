from os.path import split, splitext

from django.db.models import Model, CharField, FileField, ForeignKey

from orders.models import Order

class Categories(object):
	class Data(object):
		EXTENSIONS = (
		    '.xls',
		    '.csv',
		    '.tab',
		    '.txt',
		    '.pan',
		    '.xml',
		    '.zip')

	class Document(object):
		EXTENSIONS = (
		    '.odt',
		    '.pdf',
		    '.doc',
		    '.docx',
		    '.rtf',
		    '.zip')

	@classmethod
	def get(cls, path):
		'''
		Determines the storage category of a file, given a path to the file.
		'''
		result = None
		if not path:
			return result
		path = split(path)[1]
		ext = splitext(path)[1].lower()
		if not ext:
			return result

		for category in (cls.Data, cls.Document):
			if ext in category.EXTENSIONS:
				result = category

		return result

class StorageObject(Model):
	order = ForeignKey(Order)
	# This is currently a symlink in the project directory that will need to be
	# reorganized.
	file = FileField(upload_to='prometheus-storage')
	# Clarification: the name of the file in storage (in the case of our CouchDB
	# setup, this is the document's ID).
	name = CharField(max_length=64)
	original_name = CharField(max_length=64)
