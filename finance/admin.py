from django.contrib import admin

from .models import Invoice, InvoiceTag


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceTag)
class InvoiceTagAdmin(admin.ModelAdmin):
    pass