from django.db import models
from model_utils.models import TimeStampedModel

#managers
from .managers import ClientManager

class Documenttype(models.Model):
    type = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'documentType'
        ordering = ['pk']
        verbose_name = 'Document Type'
        verbose_name_plural = 'Documents Type'

    def __str__(self):
        return str(self.id) + '-' + self.type

# Create your models here.
class Clients(TimeStampedModel):
    name = models.CharField(max_length=50)
    cif = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5, db_column='postalCode')  # Field name made lowercase.
    invoice_code = models.CharField(max_length=3, db_column='invoiceCode', unique=True)  # Field name made lowercase.
    invoice_index = models.IntegerField(db_column='invoiceIndex')  # Field name made lowercase.
    email = models.CharField(max_length=50, unique=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    document_type = models.ForeignKey(Documenttype, db_column='documentType', on_delete=models.DO_NOTHING)

    objects = ClientManager()

    class Meta:
        managed = False
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['-name']
        #unique_together = ('cif','short_name')

    def __str__(self):
        return self.name + '-' + self.cif