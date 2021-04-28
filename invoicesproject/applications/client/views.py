from django.shortcuts import render
#
from django.views.generic import (
    ListView,
    DetailView
)

#
from .models import Clients

class ClientListView(ListView):
    template_name = "client/lista.html"
    context_object_name = 'clients'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        return context
    

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        # consulta de busqueda
        resultado = Clients.objects.search_client(kword)
        return resultado



class ClientDetailView(DetailView):
    template_name = "client/detail.html"
    model = Clients