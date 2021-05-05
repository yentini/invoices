from django.db import models
from django.db.models import Sum

class InvoiceManager(models.Manager):
    """ procedimiento para clientes """

    def search_invoices_old(self, usuario):
        # Show all clients or search by kword and user     
        return self.filter(
            user=usuario
        ).order_by('-created')

    def search_invoices(self, usuario, client, month, year):
        filters = {'user' : usuario}
        # Show all invoices or search by kword and user  
        if len(client) > 0:
            filters['invoice__client'] = client 
                       
        if month > 0:
            filters['invoice__date__month'] = month 

        if year > 0:
            filters['invoice__date__year'] = year

        return self.values('invoice__client__alias', 'invoice__date', 'invoice__code').filter(
            **filters
        ).order_by(
            'invoice'
        ).annotate(
            total_price=Sum('amount')
        )