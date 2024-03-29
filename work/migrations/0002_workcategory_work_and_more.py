# Generated by Django 5.0.1 on 2024-01-22 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='')),
                ('order', models.PositiveIntegerField()),
                ('is_visible', models.BooleanField(default=True, verbose_name='Доступно/Недоступно')),
            ],
            options={
                'verbose_name_plural': 'Work Categories',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('description', models.TextField(max_length=200, verbose_name='')),
                ('photo', models.ImageField(upload_to='work_images/', verbose_name='')),
                ('order', models.PositiveIntegerField()),
                ('is_visible', models.BooleanField(default=True, verbose_name='Доступно/Недоступно')),
                ('work_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='main_works', to='work.workcategory')),
            ],
            options={
                'verbose_name_plural': 'Works',
                'ordering': ('order',),
            },
        ),
        migrations.AddConstraint(
            model_name='work',
            constraint=models.UniqueConstraint(fields=('order', 'work_category'), name='unique_work_prt_each_work_category'),
        ),
        migrations.AlterUniqueTogether(
            name='work',
            unique_together={('id', 'slug')},
        ),
    ]
