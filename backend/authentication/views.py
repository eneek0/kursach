from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from works.models import Works
from achievements.models import Achievements
from django.views.generic.detail import DetailView

from .models import User
from .forms import UserForm, ProjectForm, AchievementForm
# Create your views here.

def index(request):
    projects = Works.objects.all()
    achievements = Achievements.objects.all()
    return render(request, 'authentication/index.html', {'projects': projects, 'achievements': achievements})

class ProjectDetailView(DetailView):
    model = Works
    template_name: 'authentication/project.html'
    context_object_name: 'project'

def achievement(request):
    achievement = Achievements.objects.order_by('id')[:1]
    return render(request, 'authentication/achievement.html', {'achievement': achievement})

def registration(request):
    error= ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else: 
            error = 'Форма была неверной'

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'authentication/registration.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.success(request, ("Произошла ошибка в ходе авторизации"))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Вы вышли из аккаунта"))
    return redirect('main')

def createProject(request):
    error= ''
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else: 
            error = 'Форма была неверной'

    form = ProjectForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'authentication/createProject.html', context)

def createAchievement(request):
    error= ''
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else: 
            error = 'Форма была неверной'

    form = AchievementForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'authentication/createAchievement.html', context)