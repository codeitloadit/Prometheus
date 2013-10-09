import datetime

from django.contrib.auth.models import User
from django.db.models import DateTimeField, ForeignKey, Model

class CreatedMixin(Model):
    created_by = ForeignKey(User, related_name='%(class)s_created_by')
    created_date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = datetime.datetime.now()

        super(CreatedMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        app_label = 'prometheus'

class ModifiedMixin(CreatedMixin):
    modified_by = ForeignKey(User, related_name='%(class)s_modified_by')
    modified_date = DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.modified_date = datetime.datetime.now()

        try:
            user = self.modified_by
            if not user:
                self.modified_by = self.created_by
        except User.DoesNotExist:
            self.modified_by = self.created_by

        super(ModifiedMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        app_label = 'prometheus'