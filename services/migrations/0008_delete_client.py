# Generated by Django 5.0.1 on 2024-01-22 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_remove_client_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
    ]
