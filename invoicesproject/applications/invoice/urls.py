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
    path(
        'invoice-detail/<pk>/', 
        views.InvoiceDetailView.as_view(),
        name='invoice-detail',
    ),
    path(
        'invoice-line-add/<pk>/', 
        views.InvoiceDetailCreateView.as_view(),
        name='invoice-line-add',
    ),
    path(
        'invoice-line-delete/<pk>/', 
        views.InvoiceLineDeleteView.as_view(),
        name='invoice-line-delete',
    ),
    path(
        'invoice-delete/<pk>/', 
        views.InvoiceDeleteView.as_view(),
        name='invoice-delete',
    ),
        path(
        'invoice-add/', 
        views.InvoiceCreateView.as_view(),
        name='invoice-add',
    ),
]