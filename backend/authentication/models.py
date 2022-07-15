from django.db import models
from achievements.models import Achievements
from faculty.models import Faculty
from works.models import Works
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255)
    email = models.EmailField(verbose_name='Email адрес', max_length=255, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=50)

    faculty = models.ForeignKey(Faculty, on_delete = models.DO_NOTHING, null=True)
    achievements = models.ManyToManyField(verbose_name='Достижения', to=Achievements, related_name='authentication')
    works = models.ManyToManyField(verbose_name='Проекты', to=Works, related_name='authentication')

    is_active = models.BooleanField(verbose_name='Активирован', default=False)
    is_staff = models.BooleanField(verbose_name='Персонал', default=False)
    is_superuser = models.BooleanField(verbose_name='Администратор', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
