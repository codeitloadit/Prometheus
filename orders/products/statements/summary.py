from django.core.urlresolvers import reverse

WORKFLOWS = {
    'statements' : {
            'description': 'Monthly, Quarterly, Semi-Annual and Annual Statements.',
            'name': 'Statements',
            'url': reverse('statements-submit')
        }
    }
