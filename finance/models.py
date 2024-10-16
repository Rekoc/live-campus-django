from django.db import models

from clients.models import Client
from finance.managers import InvoiceManager, InvoiceQuerySet, TagManager, TagQuerySet


class InvoiceTag(models.Model):
    name = models.CharField(
        "Nom du tag",
        max_length=255
    )

    objects = TagManager.from_queryset(TagQuerySet)()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Invoice(models.Model):
    tax_free_among = models.FloatField(
        "Montant HT"
    )
    taxes = models.FloatField(
        "TVA et autres taxes",
        default=20.0
    )
    name = models.CharField(
        "Nom de la facture",
        max_length=255
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="invoices",
        verbose_name="Client"
    )
    tags = models.ManyToManyField(
        InvoiceTag,
        related_name="invoices",
        null=True,
        blank=True,
    )
    has_been_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InvoiceManager.from_queryset(InvoiceQuerySet)()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"