from ckeditor.fields import RichTextField
from django.db import models


class AboutUs(models.Model):
    title = RichTextField()
    description = models.TextField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'About Header Info'

    def __str__(self):
        return f'About Header Info'


class Client(models.Model):
    description = models.TextField(max_length=250, verbose_name='Описание')
    photo = models.ImageField(upload_to='client_images/', verbose_name='Фото')
    name = models.CharField(max_length=100, verbose_name='Имя')
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Clients'
        ordering = ('order', )

    def __str__(self):
        return f'{self.name}'


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    post = models.CharField(max_length=100, verbose_name='Должность')
    photo = models.ImageField(upload_to='team_images/', verbose_name='Фото')
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Teams'
        ordering = ('order', )

    def __str__(self):
        return f'{self.name}'


class MainAboutInfo(models.Model):
    photo = models.ImageField(upload_to='about_header_images/', verbose_name='Фото')
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Main About Info'

    def __str__(self):
        return f'Main About Info'