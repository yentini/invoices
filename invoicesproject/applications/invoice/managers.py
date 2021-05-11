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

    def search_invoices(self, user, client, month, year):
        filters = {'user' : user}
        # Show all invoices or search by kword and user  
        if len(client) > 0:
            filters['invoice__client'] = client 
                       
        if month > 0:
            filters['invoice__date__month'] = month 

        if year > 0:
            filters['invoice__date__year'] = year

        return self.values('invoice__client__alias', 'invoice__date', 'invoice__code', 'invoice__id').filter(
            **filters
        ).order_by(
            'invoice'
        ).annotate(
            total_price=Sum('amount')
        )

    def search_invoice_lines(self, user, invoice_id):
        return self.filter(
            user=user,
            invoice__id=invoice_id
        ).order_by(
            'id'
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

class InvoiceManager(models.Manager):

    def search_invoice_unique(self, user, invoice_id):
        # Show all invoices or search by kword and user      
        #return super().get_queryset().filter(user=user, invoice__id=invoice_id)
        return self.filter(user=user, id=invoice_id).first()

    def search_invoices(self, user, client, month, year):
        filters = {'user' : user}
        # Show all invoices or search by kword and user  
        if len(client) > 0:
            filters['client'] = client 
                       
        if month > 0:
            filters['date__month'] = month 

        if year > 0:
            filters['date__year'] = year

        return self.values('client__alias', 'date', 'code', 'id').filter(
            **filters
        ).order_by(
            # related_name='invoice_invoiceline'
            'invoice_invoiceline__invoice'
        ).annotate(
            # related_name='invoice_invoiceline'
            #total_price=Coalesce(Sum('invoice_invoiceline__amount', output_field=FloatField()),0)
            total_price=Sum('invoice_invoiceline__amount')
        )