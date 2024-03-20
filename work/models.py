from ckeditor.fields import RichTextField
from django.db import models


class Header(models.Model):
    title = RichTextField()
    description = models.TextField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Header Work Info'

    def __str__(self):
        return f'Header Work Info'


class WorkCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='', unique=True)
    order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')

    class Meta:
        verbose_name_plural = 'Work Categories'
        ordering = ('order', )

    def __iter__(self):
        main_works = self.works.filter(is_visible=True)
        for work in main_works:
            yield work

    def __str__(self):
        return f'{self.name}'


class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name='', unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    description = models.TextField(max_length=200, verbose_name='')
    photo = models.ImageField(upload_to='work_images/', verbose_name='')
    order = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True, verbose_name='Доступно/Недоступно')
    work_category = models.ForeignKey(WorkCategory, on_delete=models.PROTECT, related_name='main_works')

    class Meta:
        verbose_name_plural = 'Works'
        ordering = ('order', )
        constraints = [
            models.UniqueConstraint(fields=['order', 'work_category'], name='unique_work_prt_each_work_category'),
        ]
        unique_together = ['id', 'slug']

    def __str__(self):
        return f'{self.title}'

