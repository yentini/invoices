from django.db import models

# Create your models here.
class Configuration(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    nif = models.CharField(max_length=20)
    owner = models.CharField(max_length=50)
    additinal_info = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'
        ordering = ['-pk']

    def __str__(self):
        return str(self.id)


class ClientConfiguration(models.Model):
    default_irpf = models.IntegerField()

    class Meta:
        verbose_name = 'ClientConfiguration'
        verbose_name_plural = 'ClientConfigurations'
        ordering = ['-pk']

    def __str__(self):
        return str(self.id)