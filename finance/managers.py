from django.db import models


class ClientManager(models.Manager):
    pass


class ClientQuerySet(models.QuerySet):
    pass


class InvoiceManager(models.Manager):
    pass


class InvoiceQuerySet(models.QuerySet):
    pass


class TagManager(models.Manager):
    pass


class TagQuerySet(models.QuerySet):
    pass