from datetime import datetime

from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from finance.models import Invoice


class InvoiceListView(LoginRequiredMixin, ListView):
    permission_required = ("view_invoice",)
    model = Invoice
    queryset = Invoice.objects.all()
    template_name = "finance/list.html"
    paginate_by = 10


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    permission_required = ("view_invoice",)
    model = Invoice
    template_name = "finance/detail.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["now"] = datetime.now()
        return context