# Generated by Django 5.0.1 on 2024-01-22 16:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_remove_work_unique_work_prt_each_work_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('envato_link', models.URLField(max_length=255, verbose_name='Envato')),
                ('facebook_link', models.URLField(max_length=255, verbose_name='Facebook')),
                ('skype_link', models.URLField(max_length=255, verbose_name='Skype')),
                ('twitter_link', models.URLField(max_length=255, verbose_name='Twitter')),
                ('whatsapp_link', models.URLField(max_length=255, verbose_name='Whatsapp')),
                ('copyright_text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Footer Info',
            },
        ),
    ]
