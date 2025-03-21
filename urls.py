from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),  # Add this line for the root URL
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/todo/', views.todo_list, name='todo_list'),
    path('todo/add/', views.add_todo, name='add_todo'),
    path('about/', views.about, name='about'),
]