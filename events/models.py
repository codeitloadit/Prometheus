from __future__ import absolute_import

from django.db.models import CharField, Model

from mixins import CreatedMixin

class Event(CreatedMixin):
    name = CharField(max_length=16, blank=False, null=False)
    # Maybe a format method on the name instead?
    # label = CharField()
    message = CharField(max_length=120)

    class Meta:
        abstract = True

    def equals(self, other):
        '''
        Returns True when `self` and `other` refer to the same model instance.
        '''
        return self.pk == other.pk
