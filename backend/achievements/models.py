from django.db import models
from organization.models import Organization
from professor.models import Professor

class Achievements(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    professor = models.ManyToManyField(verbose_name='Преподаватель', to=Professor, related_name='achievements')
    organization = models.OneToOneField(Organization, verbose_name='Мероприятие', on_delete = models.CASCADE, related_name='achievements')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'
