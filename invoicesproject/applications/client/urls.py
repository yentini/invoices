#
from django.urls import path
from . import views

app_name = "client_app"

urlpatterns = [
    path(
        'clients/', 
        views.ClientListView.as_view(),
        name='client-list',
    ),
    path(
        'client/<pk>/', 
        views.ClientDetailView.as_view(),
        name='client-detail',
    ),
    path(
        'update-client/<pk>/',
        views.ClientUpdateView.as_view(),
        name = 'client-update'
    ),
    path(
        'delete-client/<pk>/',
        views.ClientDeleteView.as_view(),
        name = 'client-delete'
    ),
    path(
        'add-client/', 
        views.ClientCreateView.as_view(),
        name='client-add'
    ),
]