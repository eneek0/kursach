from distutils.command.upload import upload
from trace import CoverageResults
from django.db import models
from professor.models import Professor

class Works(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    cover = models.ImageField(verbose_name='Обложка', upload_to='works/covers')
    professor = models.ManyToManyField(verbose_name='Преподаватель', to=Professor, related_name='works')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
