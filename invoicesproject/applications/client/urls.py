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
        'entrada/<pk>/', 
        views.ClientDetailView.as_view(),
        name='client-detail',
    ),
]