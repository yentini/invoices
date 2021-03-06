# Generated by Django 3.2 on 2021-05-03 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_invoice', to='client.client')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_invoice', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
                'ordering': ['-user', '-created'],
                'unique_together': {('user', 'code')},
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.FloatField()),
                ('net_amount', models.FloatField()),
                ('irpf', models.FloatField()),
                ('irpf_amount', models.FloatField()),
                ('iva', models.FloatField()),
                ('iva_amount', models.FloatField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_invoiceline', to='invoice.invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_invoiceline', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invoice Line',
                'verbose_name_plural': 'Invoice Lines',
                'ordering': ['-invoice', '-created'],
            },
        ),
    ]
