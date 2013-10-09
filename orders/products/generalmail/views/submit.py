from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.defaults import RequestContext
from django.views.generic.edit import ProcessFormView

from accounts.models import Account
from orders.forms import NewOrderForm
from orders.products.generalmail.forms import NewGeneralMailNestedForm

class Submit(ProcessFormView):
    # Commenting this to remind myself: if you want to do something before
    # method-specific code is run, do it here.
#    def dispatch(self, request, *args, **kwargs):
#        super(Submit, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Going with an unbound form.
        context = {'order_form': NewOrderForm(prefix='order-form') }
        context.update(NewGeneralMailNestedForm().subforms_dict())
        return render_to_response('orders/new.html',
            context_instance=RequestContext(request, context))

    def post(self, request, *args, **kwargs):
        order_form = NewOrderForm(request.POST, prefix='order-form')
        if not order_form.is_valid():
            context = { 'order_form': order_form }
            context.update(NewGeneralMailNestedForm(request.POST).subforms_dict())
            return render_to_response('orders/new.html',
                context_instance=RequestContext(request, context))

        order = order_form.save(commit=False)
        order.customer = Account.objects.get(slug='optimaloutsource')
        order.created_by = request.user

        form = NewGeneralMailNestedForm(request.POST, request.FILES, order)
        if form.is_valid():
            order.save()
            form.save()
        else:
            return HttpResponse('Failure!')
        return HttpResponse('Success!')