from django.db import models


class ClientManager(models.Manager):
    """ procedimiento para clientes """

    def search_client(self, kword, usuario):
        # Show all clients or search by kword and user     
        return self.filter(
            name__icontains=kword,
            user=usuario
        ).order_by('-created')