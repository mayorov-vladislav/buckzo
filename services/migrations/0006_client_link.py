# Generated by Django 5.0.1 on 2024-01-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_client_name_alter_client_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='link',
            field=models.URLField(default=0, max_length=100, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
