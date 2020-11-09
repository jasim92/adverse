from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'Home'),
    path('register/', views.handleRegister, name= 'Register'),
    path('login/', views.handleLogin, name= 'Login'),
    path('logout/', views.handleLogout, name= 'logout'),

]