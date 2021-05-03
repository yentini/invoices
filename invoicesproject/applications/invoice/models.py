from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

from applications.client.models import Client


# Create your models here.
class Invoice(TimeStampedModel):
    code = models.CharField(max_length=50)  
    date = models.DateField()
    client = models.ForeignKey(
        Client,
        related_name='client_invoice',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_invoice',
        on_delete=models.CASCADE,
    )

    #objects = InvoiceManager()

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['-user', '-created']
        unique_together = ('user','code')
    
    def __str__(self):
        return self.code

class InvoiceLine(TimeStampedModel):
    amount = models.FloatField()
    net_amount = models.FloatField()
    irpf = models.FloatField()
    irpf_amount = models.FloatField()    
    iva = models.FloatField()
    iva_amount = models.FloatField()
    invoice = models.ForeignKey(
        Invoice,
        related_name='invoice_invoiceline',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_invoiceline',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Invoice Line'
        verbose_name_plural = 'Invoice Lines'
        ordering = ['-invoice', 'created']
    
    def __str__(self):
        return self.invoice.code + '-' + str(self.id)