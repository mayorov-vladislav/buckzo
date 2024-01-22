from django.db import models


class Header(models.Model):
    title = models.CharField(max_length=200, verbose_name="Начало заголовка")
    head_words = models.CharField(max_length=200, verbose_name="Главное слово", blank=True)
    title2 = models.CharField(max_length=200, verbose_name="Конец заголовка", blank=True)
    description = models.TextField(max_length=250, verbose_name="Описание")

    class Meta:
        verbose_name_plural = 'Services Header Info'

    def __str__(self):
        return f'Services Header Info'


class ServiceInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(max_length=250, verbose_name="Описание")
    order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name="Доступно/Недоступно")

    class Meta:
        verbose_name_plural = 'Services Info'
        ordering = ('order', )

    def __str__(self):
        return f'{self.title}'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    photo = models.ImageField(upload_to='client_images/', verbose_name="Фото")
    link = models.URLField(max_length=100, verbose_name="Ссылка", )
    order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name="Доступно/Недоступно")

    class Meta:
        verbose_name_plural = 'Clients'
        ordering = ('order', )

    def __str__(self):
        return f'{self.name}'

