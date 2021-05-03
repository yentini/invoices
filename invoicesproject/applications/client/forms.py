from django import forms

from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = (
            'name',
            'alias',
            'document_type',
            'cif',
            'address',
            'city',
            'province',
            'postal_code',
            'invoice_code',
            'invoice_index',
            'email',
        )
        widgets = {
            'name' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Introduce un nombre aquí',
                }
            )
        }