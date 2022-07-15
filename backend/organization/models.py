from django.db import models

# Create your models here.

class Organization(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    name_of_sponsor = models.CharField(verbose_name='Организатор', max_length=255)
    email = models.EmailField(verbose_name='Email адрес', max_length=255)
    address = models.CharField(verbose_name='Адрес', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
