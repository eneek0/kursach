from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('registration', views.registration, name='registration'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project'),
    path('achievement', views.achievement, name='achievement'),
    path('createProject', views.createProject, name='createProject'),
    path('createAchievement', views.createAchievement, name='createAchievement'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)