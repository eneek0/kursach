from achievements.models import Achievements
from .models import User, Works
from django.forms import ModelForm, TextInput, DateInput, Textarea, SelectMultiple, Select

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "middle_name", "password"]
        widgets = {
            "email": TextInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Введите e-mail'
            }),
            "first_name": TextInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Введите имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Введите фамилию'
            }),
            "middle_name": TextInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Введите отчество'
            }),
            "password": TextInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Введите пароль',
                'type': 'password'
            }),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Works
        fields = ["title", "description", "professor", "date"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Название проекта'
            }),
            "description": Textarea(attrs={
                'class': 'form__textarea', 
                'placeholder': 'Описание проекта'
            }),
            "professor": SelectMultiple(attrs={
                'class': 'form__input', 
                'placeholder': 'Преподаватель'
            }),
            "date": DateInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Дата'
            }),
        }

class AchievementForm(ModelForm):
    class Meta:
        model = Achievements
        fields = ["title", "description", "professor", "date", "organization"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Название достижения'
            }),
            "description": Textarea(attrs={
                'class': 'form__textarea', 
                'placeholder': 'Описание достижения'
            }),
            "professor": SelectMultiple(attrs={
                'class': 'form__input', 
                'placeholder': 'Преподаватель'
            }),
            "date": DateInput(attrs={
                'class': 'form__input', 
                'placeholder': 'Дата'
            }),
            "organization": Select(attrs={
                'class': 'form__input', 
                'placeholder': 'Организация'
            }),
        }