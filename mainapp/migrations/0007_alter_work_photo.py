# Generated by Django 5.0.1 on 2024-01-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_work_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='photo',
            field=models.ImageField(upload_to='works_image/', verbose_name='Фото'),
        ),
    ]
