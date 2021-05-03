from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

#managers
from .managers import ClientManager

class Documenttype(models.Model):
    type = models.CharField(max_length=25)

    class Meta:     
        ordering = ['pk']
        verbose_name = 'Document Type'
        verbose_name_plural = 'Documents Type'

    def __str__(self):
        return self.type

# Create your models here.
class Client(TimeStampedModel):
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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_client',
        on_delete=models.CASCADE,
    )

    objects = ClientManager()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['-name']
        unique_together = ('cif','name')

    def __str__(self):
        return self.name + '-' + self.cif

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)