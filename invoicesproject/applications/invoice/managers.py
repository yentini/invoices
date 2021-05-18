from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import FloatField

class InvoiceLineManager(models.Manager):
    """ procedimiento para clientes """

    def search_all_invoices(self, user):
        filters = {'user' : user}
        # Show all invoices or search by kword and user          
        return self.values('invoice__client__alias', 'invoice__date', 'invoice__code').filter(
            **filters
        ).order_by(
            'invoice'
        ).annotate(
            total_price=Sum('amount')
        )
    
    def search_invoice(self, user, invoice_id):
        # Show all invoices or search by kword and user          
        return self.values('invoice__client__alias', 'invoice__date', 'invoice__code', 'invoice__id').filter(
            user=user,
            invoice__id=invoice_id
        ).order_by(
            'invoice'
        ).annotate(
            total_price=Sum('amount')
        ).first()

    def sum_total(self, user, client, month, year):
        filters = {'user' : user}
        if len(client) > 0:
            filters['invoice__client'] = client

        if month > 0:
            filters['invoice__date__month'] = month 

        if year > 0:
            filters['invoice__date__year'] = year


        # Show all invoices or search by kword and user          
        return self.filter(
            **filters
        ).aggregate(
            total_price=Sum('amount'),
            total_irpf_amount=Sum('irpf_amount'),
            total_iva_amount=Sum('iva_amount'),
            total_net_amount=Sum('net_amount'),
        )

class InvoiceManager(models.Manager):

    def search_invoice_unique(self, user, invoice_id):
        # Show all invoices or search by kword and user      
        #return super().get_queryset().filter(user=user, invoice__id=invoice_id)
        return self.filter(user=user, id=invoice_id).first()

    def search_invoice(self, user, invoice_id):
        # Show all invoices or search by kword and user          
        return self.values('client__alias', 'date', 'code', 'id').filter(
            user=user,
            id=invoice_id
        ).order_by(
            'invoice_invoiceline__invoice'
        ).annotate(
            total_amount=Sum('invoice_invoiceline__amount'),
            total_net_amount=Sum('invoice_invoiceline__net_amount'),
            total_irpf_amount=Sum('invoice_invoiceline__irpf_amount'),
            total_iva_amount=Sum('invoice_invoiceline__iva_amount'),
        ).first()

    def search_invoices(self, user, client, month, year):
        filters = {'user' : user}
        # Show all invoices or search by kword and user  
        if len(client) > 0:
            filters['client'] = client 
                       
        if month > 0:
            filters['date__month'] = month 

        if year > 0:
            filters['date__year'] = year

        return self.values('client__alias', 'client__id','date', 'code', 'id').filter(
            **filters
        ).order_by(
            # related_name='invoice_invoiceline'
            'invoice_invoiceline__invoice'
        ).annotate(
            # related_name='invoice_invoiceline'
            total_amount=Sum('invoice_invoiceline__amount'),
            total_net_amount=Sum('invoice_invoiceline__net_amount'),
            total_irpf_amount=Sum('invoice_invoiceline__irpf_amount'),
            total_iva_amount=Sum('invoice_invoiceline__iva_amount'),
        )

    def search_invoice_lines(self, user, invoice_id):

        return self.values(
            'invoice_invoiceline__amount', 
            'invoice_invoiceline__net_amount',
            'invoice_invoiceline__irpf',
            'invoice_invoiceline__irpf_amount',
            'invoice_invoiceline__iva',
            'invoice_invoiceline__iva_amount',
            'invoice_invoiceline__id'
        ).filter(
            user=user,
            id=invoice_id
        ).prefetch_related('invoice_invoiceline')