from django.db import models


class ClientManager(models.Manager):
    """ procedimiento para entrada """

    def search_client(self, kword):
        # Show all clients or search by kword        
        return self.filter(
            title__icontains=kword,
            public=True
        ).order_by('-created')