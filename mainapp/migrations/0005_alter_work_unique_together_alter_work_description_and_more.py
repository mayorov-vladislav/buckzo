# Generated by Django 5.0.1 on 2024-01-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_workcategory_work_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='work',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='work',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Доступно/Недотсупно'),
        ),
        migrations.AlterField(
            model_name='work',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='work',
            name='photo',
            field=models.ImageField(upload_to='main_works_image/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='work',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='workcategory',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Доступно/Недотсупно'),
        ),
        migrations.AlterField(
            model_name='workcategory',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterUniqueTogether(
            name='work',
            unique_together={('name', 'slug')},
        ),
    ]