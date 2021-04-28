# Generated by Django 3.2 on 2021-04-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('value', models.CharField(max_length=100, verbose_name='Value')),
            ],
            options={
                'db_table': 'configuration',
                'ordering': ['pk'],
                'managed': False,
            },
        ),
    ]