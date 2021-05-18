from django.contrib import admin
from .models import Configuration, ClientConfiguration

# Register your models here.

admin.site.register(Configuration)
admin.site.register(ClientConfiguration)