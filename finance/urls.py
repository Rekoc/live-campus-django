from django.urls import path

from .views import (
    InvoiceDetailView,
    InvoiceListView
)


app_name = "finance"
urlpatterns = [
    path("<int:pk>", view=InvoiceDetailView.as_view(), name="finance-detail"),
    path("", view=InvoiceListView.as_view(), name="finance-list"),
]