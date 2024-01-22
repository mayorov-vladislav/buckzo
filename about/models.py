from django.db import models


class AboutHeader(models.Model):
    title = models.CharField(max_length=100, verbose_name='Начало заголовка')
    job1 = models.CharField(max_length=100, verbose_name='1 Профессия', blank=True)
    job2 = models.CharField(max_length=100, verbose_name='2 Профессия', blank=True)
    char = models.CharField(max_length=100, verbose_name='Знак')
    title2 = models.CharField(max_length=100, verbose_name='Конец заголовка', blank=True)
    description = models.TextField(max_length=200, verbose_name='Описание')
    title3 = models.CharField(max_length=100, verbose_name='Подзаголовок', blank=True)
    head_words = models.CharField(max_length=100, verbose_name='Главное слово', blank=True)
    title4 = models.CharField(max_length=100, verbose_name='Конец подзаголовка', blank=True)

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