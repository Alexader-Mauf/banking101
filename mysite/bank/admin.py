from django.contrib import admin
from .models import Account,Transfer,Customer
# Register your models here.
admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Customer)
