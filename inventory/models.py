
from django.db.models import CharField, Model

class BaseInventory(Model):
    label = CharField(max_length=64, primary_key=True)
    description = CharField(max_length=128)

class StatementStock(BaseInventory):
    length = CharField(max_length=2, choices=(('11', '11"'), ('14', '14"')))

    # You could expand this model to handle the statement stock naming
    # convention.

_COLORED_STOCK_CHOICES = (('White', 'White'),
    ('Goldenrod', 'Goldenrod'),
    ('Orchid', 'Orchid'))

class ColoredStock(BaseInventory):
    color = CharField(max_length=16, choices=_COLORED_STOCK_CHOICES)