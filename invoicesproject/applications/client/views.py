from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
)

#
from .models import Client

#forms
from .forms import ClientForm

class ClientListView(LoginRequiredMixin, ListView):
    template_name = "client/list.html"
    context_object_name = 'clients'
    paginate_by = 8
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        # consulta de busqueda
        resultado = Client.objects.search_client(kword, self.request.user)
        return resultado


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "client/add.html"
    form_class = ClientForm
    success_url = reverse_lazy('client_app:client-list')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        print("******************ddddddddd********************")
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super(ClientCreateView, self).form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "client/update.html"
    fields = [
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
        'email'
    ]
    success_url = reverse_lazy('client_app:client-list')
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context['client_name'] = self.get_object().name
        return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         print(request.POST['invoice_index'])
#         return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # recuperar el usuario
        print(form.cleaned_data['name'])
        print(self.request.user)
        return super(ClientUpdateView, self).form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    template_name = "client/detail.html"
    model = Client
    login_url = reverse_lazy('users_app:user-login')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "client/delete.html"
    success_url = reverse_lazy('client_app:client-list')
    login_url = reverse_lazy('users_app:user-login')