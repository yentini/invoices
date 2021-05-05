from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime
import calendar
import locale

#
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
)

from .models import InvoiceLine
from applications.client.models import Client


# Create your views here.
class InvoiceListView(LoginRequiredMixin, ListView):
    template_name = "invoice/list.html"
    context_object_name = 'invoices'
    paginate_by = 8
    login_url = reverse_lazy('users_app:user-login')

    locale.setlocale(locale.LC_ALL, '')

    def get_context_data(self, **kwargs):
        months = set()
        context = super(InvoiceListView, self).get_context_data(**kwargs)
        context["clients"] = Client.objects.all()   
        for invoice in context["invoices"]:
            months.add(invoice["invoice__date"].month)
        
        months_name = set()
        for month in months:
            months_name.add(calendar.month_name[month].capitalize())
        context["months"] = months_name

        return context
    
    def get_queryset(self):
        # consulta de busqueda
        client = self.request.GET.get("client", '')
        month = self.request.GET.get("months", '')
        year = self.request.GET.get("years", '')
        month_number = list(calendar.month_name).index(month.lower())
        #print(list(calendar.month_name))
        resultado = InvoiceLine.objects.search_invoices(self.request.user, client, month_number,0)
        return resultado
