from django.db import models

# Create your models here.
class Configuration(models.Model):
    name = models.CharField('Name', max_length=50)
    value = models.CharField('Value', max_length=100)

    class Meta:
        managed = False
        ordering = ['pk']
        db_table = 'configuration'

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.value