from django.db import models

from clients.managers import ClientManager, ClientQuerySet


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"