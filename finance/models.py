from django.db import models

from finance.managers import ClientManager, ClientQuerySet, InvoiceManager, InvoiceQuerySet, TagManager, TagQuerySet


class Client(models.Model):
    name = models.CharField(
        "Nom du client",
        max_length=255
    )
    tax_number = models.CharField(
        "Numéro TVA",
        max_length=255
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ClientManager.from_queryset(ClientQuerySet)()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class InvoiceTag(models.Model):
    name = models.CharField(
        "Nom du tag",
        max_length=255
    )

    objects = TagManager.from_queryset(TagQuerySet)()

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
        related_name="invoices"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InvoiceManager.from_queryset(InvoiceQuerySet)()

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"