from django.core.validators import RegexValidator
from django.db import models


class Header(models.Model):
    title1 = models.CharField(max_length=100, blank=True, verbose_name="Начало заголовка")
    title2 = models.CharField(max_length=100, blank=True, verbose_name="Конец заголовка")
    description = models.TextField(max_length=250, verbose_name="")

    class Meta:
        verbose_name_plural = 'Contact Header Info'

    def __str__(self):
        return f'Contact Header Info'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    photo = models.ImageField(upload_to='contact/client_images', verbose_name='Фото')
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')

    class Meta:
        verbose_name_plural = 'Clients Info'
        ordering = ('order', )

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Subhect')
    message = models.TextField(max_length=500, verbose_name='Сообщение', blank=True)
    is_precessed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactUs(models.Model):
    email_app = models.CharField(max_length=100, verbose_name='Почта приложения')
    phone_app = models.CharField(max_length=100, verbose_name='Номер приложения')
    address_app = models.CharField(max_length=100, verbose_name='Адрес')

    class Meta:
        verbose_name_plural = 'Contact Us Info'

    def __str__(self):
        return f'Contact Us Info'

