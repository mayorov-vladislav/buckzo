# Generated by Django 5.0.1 on 2024-01-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=100, verbose_name='Начало заголовка')),
                ('title2', models.CharField(blank=True, max_length=100, verbose_name='Конец заголовка')),
                ('description', models.TextField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Header Work Info',
            },
        ),
    ]
