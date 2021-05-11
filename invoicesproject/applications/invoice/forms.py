from django import forms

from .models import InvoiceLine

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