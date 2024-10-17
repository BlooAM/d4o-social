from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView, name='logout'),
    path('', views.dashboard, name='dashboard'),
]
