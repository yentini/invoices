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

from .models import InvoiceLine, Invoice
from applications.client.models import Client
from .forms import InvoiceLineForm


# Create your views here.
class InvoiceListView(LoginRequiredMixin, ListView):
    template_name = "invoice/list.html"
    context_object_name = 'invoices'
    paginate_by = 8
    login_url = reverse_lazy('users_app:user-login')

    locale.setlocale(locale.LC_ALL, '')

    def get_context_data(self, **kwargs):        
        context = super(InvoiceListView, self).get_context_data(**kwargs)
        # Clients
        context["clients"] = Client.objects.all()  

        # Months and years 
        months = set()
        years = set()
        months_name = set()

        invoices = InvoiceLine.objects.search_all_invoices(self.request.user)

        for invoice in invoices:
            months.add(invoice["invoice__date"].month)
            years.add(invoice["invoice__date"].year)
        for month in months:
            months_name.add(calendar.month_name[month].capitalize())

        context["months"] = months_name
        context["years"] = years

        # Current parameters
        context["current_year"] = self.request.GET.get("years", '')
        context["current_month"] = self.request.GET.get("months", '')
        context["current_client"] = self.request.GET.get("client", '')

        return context
    
    def get_queryset(self):
        # consulta de busqueda
        client = self.request.GET.get("client", '')
        month = self.request.GET.get("months", '')
        year = self.request.GET.get("years", '') if self.request.GET.get("years", '') != '' else '0'
        month_number = list(calendar.month_name).index(month.lower())
        resultado = Invoice.objects.search_invoices(self.request.user, client, month_number, int(year))
        return resultado


class InvoiceDetailView(LoginRequiredMixin, ListView):
    template_name = "invoice/detail.html"
    context_object_name = 'invoice_lines'
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):        
        context = super(InvoiceDetailView, self).get_context_data(**kwargs)
        # Invoice
        context["invoice"] = Invoice.objects.search_invoice(self.request.user, self.kwargs['pk'])
        return context

    def get_queryset(self):
        # consulta de busqueda
        resultado = Invoice.objects.search_invoice_lines(self.request.user, self.kwargs['pk'])
        print(resultado)
        return resultado


class InvoiceDetailCreateView(LoginRequiredMixin, CreateView):
    model = InvoiceLine
    template_name = "invoice/add_line.html"
    form_class = InvoiceLineForm
    #success_url = reverse_lazy('invoice_app:invoice-detail', kwargs={'pk': kwargs['pk']})
    login_url = reverse_lazy('users_app:user-login')

    def setup(self, request, *args, **kwargs):
        super(InvoiceDetailCreateView, self).setup(request, *args, **kwargs)
        self.success_url = reverse_lazy('invoice_app:invoice-detail', kwargs={'pk': self.kwargs['pk']})
        

    def get_context_data(self, **kwargs):        
        context = super(InvoiceDetailCreateView, self).get_context_data(**kwargs)
        # Invoice
        context["invoice"] = InvoiceLine.objects.search_invoice(self.request.user, self.kwargs['pk'])
        context["invoice_lines"] = Invoice.objects.search_invoice_lines(self.request.user, self.kwargs['pk'])
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        invoice_line = form.save(commit=False)

        invoice_unique = Invoice.objects.search_invoice_unique(self.request.user, self.kwargs['pk'])

        invoice_line.invoice = invoice_unique
        invoice_line.user = self.request.user
        invoice_line.save()
        return super(InvoiceDetailCreateView, self).form_valid(form)


class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    login_url = reverse_lazy('users_app:user-login')
    success_url = reverse_lazy('invoice_app:invoice-list')


class InvoiceLineDeleteView(LoginRequiredMixin, DeleteView):
    model = InvoiceLine
    login_url = reverse_lazy('users_app:user-login')

    def setup(self, request, *args, **kwargs):
        super(InvoiceLineDeleteView, self).setup(request, *args, **kwargs)
        invoice_line = InvoiceLine.objects.filter(id=self.kwargs['pk']).first()
        self.success_url = reverse_lazy('invoice_app:invoice-detail', kwargs={'pk': invoice_line.invoice.id})