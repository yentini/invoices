#
from django.urls import path
from . import views

app_name = "invoice_app"

urlpatterns = [
    path(
        'invoices/', 
        views.InvoiceListView.as_view(),
        name='invoice-list',
    ),
]