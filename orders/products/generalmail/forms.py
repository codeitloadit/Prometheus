from uuid import uuid4

from django.forms import CharField, Form, Textarea

from addresses.models import Address
from orders.products.generalmail.models import GeneralMail
from storageobjects.forms import StorageFormset
from storageobjects.models import Categories, StorageObject

class NewGeneralMailForm(Form):
    return_address = CharField(widget=Textarea(attrs={ 'cols': 64, 'rows': 5 }))

class NewGeneralMailNestedForm(object):
    '''
    Experimental Form-like object that uses other forms.

    The subforms validate themselves normally. The value added is that this
    object validates the forms against each other, but still acts like a single
    form when possible.

    Also, it's designed to save the models it interacts with (like a ModelForm)
    so that the view isn't saddled with the responsibility.
    '''

    def __init__(self, data=None, files=None, order=None):
        self.order = order
        self.gm_form = NewGeneralMailForm(data, prefix='gm-form')
        self.files_formset = StorageFormset(data, files, prefix='files-form')

    def is_valid(self):
        # Validates at the individual form level. Note that we aren't
        # validating the actual models right now, just the form data.
        result = self.gm_form.is_valid() and self.files_formset.is_valid()
        if result:
            # This address needs to validate according to the model's rules to be
            # accepted.
            self.return_address = Address.from_multiline_string(
                self.gm_form.cleaned_data['return_address'])

            result = ((not self.return_address.is_empty) and
                self._validate_files(self.files_formset))

        return result

    def save(self, commit=True):
        self.return_address.save()
        product = GeneralMail(order=self.order, return_address=self.return_address)
        product.save()

        for form in self.files_formset:
            obj = StorageObject(order=self.order)
            obj.file = form.cleaned_data['file']
            obj.original_name = form.cleaned_data['file'].name
            # TODO: Replace this with actual IDs if real storage is implemented.
            obj.name = str(uuid4())
            obj.save()

    def subforms_dict(self):
        # Returns the forms needed for this product.
        # - Used to return only unbound forms but it will be better to return
        # - the forms in the current state to handle errors.
        #
        # Use this to update your view's context with the forms needed for this product.
        # This model will be responsible for validating the bound forms.
        return { 'gm_form': self.gm_form, 'files_form': self.files_formset }

    def _validate_files(self, files_formset):
        # Expects that cleaned_data is available, such as by having called
        # is_valid() ahead.

        found_data = False
        found_document = False

        for form in files_formset:
            filename = form.cleaned_data['file'].name
            category = Categories.get(filename)
            if category == Categories.Data:
                found_data = True
            elif category == Categories.Document:
                found_document = True

        return found_data and found_document

