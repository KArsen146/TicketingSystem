from django.contrib import admin

# Register your models here.
from user.models import Manager, Cashier

admin.site.register(Manager)
admin.site.register(Cashier)
