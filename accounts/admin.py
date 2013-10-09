from django.contrib.admin import ModelAdmin, site

from models import Account

class AccountAdmin(ModelAdmin):
    list_display = 'name', 'slug',

site.register(Account, AccountAdmin)