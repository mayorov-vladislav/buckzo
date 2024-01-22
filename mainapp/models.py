from ckeditor.fields import RichTextField
from django.db import models


class Header(models.Model):
    title = models.CharField(max_length=100, verbose_name='Начало заголовка')
    job1 = models.CharField(max_length=100, verbose_name='1 Профессия', blank=True)
    job2 = models.CharField(max_length=100, verbose_name='2 Профессия', blank=True)
    char = models.CharField(max_length=100, verbose_name='Знак', blank=True)
    title2 = models.CharField(max_length=100, verbose_name='Конец заголовка', blank=True)
    description = models.TextField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Header Info'

    def __str__(self):
        return f'Header Info'


class MainInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=255, verbose_name='Описание')
    order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')

    class Meta:
        verbose_name_plural = 'Main Info'
        ordering = ('order', )

    def __str__(self):
        return f'{self.title}'


class WorkCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недотсупно')

    class Meta:
        verbose_name_plural = 'Work Categories'
        ordering = ('order', )

    def __iter__(self):
        works = self.works.filter(is_visible=True)
        for work in works:
            yield work

    def __str__(self):
        return f'{self.name}'


class Work(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='works_image/', verbose_name='Фото')
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недотсупно')
    order = models.PositiveSmallIntegerField()
    work_category = models.ForeignKey(WorkCategory, on_delete=models.PROTECT, related_name='works')

    class Meta:
        verbose_name_plural = 'Works'
        ordering = ('order', )
        constraints = [
            models.UniqueConstraint(fields=['order', 'work_category'], name='unique_work_prt_each_main_work_category'),
        ]
        unique_together = ['id', 'slug']

    def __str__(self):
        return f'{self.name}'


class Footer(models.Model):
    envato_link = models.URLField(max_length=255, verbose_name='Envato')
    facebook_link = models.URLField(max_length=255, verbose_name='Facebook')
    skype_link = models.URLField(max_length=255, verbose_name='Skype')
    twitter_link = models.URLField(max_length=255, verbose_name='Twitter')
    whatsapp_link = models.URLField(max_length=255, verbose_name='Whatsapp')
    copyright_text = RichTextField()

    class Meta:
        verbose_name_plural = 'Footer Info'

    def __str__(self):
        return f'Footer Info'
