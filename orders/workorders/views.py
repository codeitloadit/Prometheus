from django.views.generic import CreateView

from orders.workorders import forms

class NewWorkOrderView(CreateView):
    template_name = 'orders/workorders/new.html'

    def get_form_class(self):
        classname_from_url = self.kwargs['workorderclass'] + 'form'
        form_class = None

        for attr in dir(forms):
            if attr.lower() == classname_from_url:
                form_class = getattr(forms, attr)
                break

        return form_class
