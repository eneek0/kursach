from django.db import models

# Create your models here.
class Faculty(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    number = models.IntegerField(verbose_name='Номер', default=0)
    email = models.EmailField(verbose_name='Email адрес', max_length=255)
    number_of_students = models.IntegerField(verbose_name='Количество студентов', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
