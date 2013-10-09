from django.forms import FileField, Form
from django.forms.models import formset_factory

class StorageForm(Form):
    file = FileField()

StorageFormset = formset_factory(StorageForm, extra=2)

