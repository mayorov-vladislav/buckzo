# Generated by Django 5.0.1 on 2024-01-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('photo', models.ImageField(upload_to='contact/client_images', verbose_name='')),
                ('order', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True, verbose_name='Доступно/Недоступно')),
            ],
            options={
                'verbose_name_plural': 'Clients Info',
                'ordering': ('order',),
            },
        ),
    ]
