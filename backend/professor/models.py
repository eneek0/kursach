from django.db import models

# Create your models here.

class Professor(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255)
    email = models.EmailField(verbose_name='Email адрес', max_length=255)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(verbose_name='Фото', upload_to='professors')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
