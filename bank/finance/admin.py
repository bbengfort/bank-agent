from django.contrib import admin
from finance.models import Account, Owner, Transfer

# Register your models here.
admin.site.register(Account)
admin.site.register(Owner)
admin.site.register(Transfer)