# Generated by Django 5.0.1 on 2024-01-22 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_alter_client_name_alter_client_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address_app',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email_app',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone_app',
        ),
    ]