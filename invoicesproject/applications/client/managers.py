from django.db import models


class ClientManager(models.Manager):
    """ procedimiento para clientes """

    def search_client(self, kword):
        # Show all clients or search by kword        
        return self.filter(
            name__icontains=kword
        )