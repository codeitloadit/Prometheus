import settings

from importlib import import_module
from os.path import join
from pkgutil import walk_packages

from django.db.models import get_app

PRODUCT_CHOICES = (('generalmail', 'General Mail'), ('statements', 'Statements'),)

def product_app_names():
    path = [ join(settings.APP_PATH, 'orders', 'products') ]
    return [ x[1] for x in walk_packages(path) if x[2] ]

def summary_modules():
    result = []
    products = product_app_names()
    for product_name in products:
        mod = None
        try:
            mod = import_module('orders.products.{0}.summary'.format(product_name))
        except ImportError:
            continue

        result.append(mod)

    return result
