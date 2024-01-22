# Generated by Django 5.0.1 on 2024-01-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('post', models.CharField(max_length=100, verbose_name='Должность')),
                ('photo', models.ImageField(upload_to='team_images/', verbose_name='Фото')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Доступно/Недоступно')),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'ordering': ('order',),
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Доступно/Недоступно'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to='client_images/', verbose_name='Фото'),
        ),
    ]