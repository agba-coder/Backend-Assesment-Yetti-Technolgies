
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ... add other URL patterns ...
    path("", views.hello_world, name='hello_world'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
