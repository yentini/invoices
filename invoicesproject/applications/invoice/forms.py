from django import forms
from django.forms.fields import DateField

from .models import InvoiceLine, Invoice

class InvoiceLineForm(forms.ModelForm):

    class Meta:
        model = InvoiceLine
        fields = (
            'amount',
            'net_amount',
            'irpf',
            'irpf_amount',
            'iva',
            'iva_amount',
        )


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = (
            'code',
            'client',
            'date',
        )
        widgets = {
            'date' : forms.DateTimeInput(attrs={
                'type': 'date',
             })
        }