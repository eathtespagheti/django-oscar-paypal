from django.contrib import admin
from itertools import chain

from paypal import models

@admin.register(models.CheckoutTransaction)
class CheckoutTransactionAdmin(admin.ModelAdmin):
    readonly_fields = list(set(chain.from_iterable(
        (field.name, field.attname) if hasattr(field, 'attname') else (field.name,)
        for field in models.CheckoutTransaction._meta.get_fields()
    )))
