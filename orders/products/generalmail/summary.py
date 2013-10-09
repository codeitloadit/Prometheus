from django.core.urlresolvers import reverse

WORKFLOWS = {
    'generalmail' : {
            'description': 'Perfect for one-off Newsletters, Audits and Budgets.',
            'name': 'General Mail',
            'url': reverse('generalmail-submit')
        }
    }

