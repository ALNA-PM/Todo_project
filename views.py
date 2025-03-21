# Create your views here.
# todo_app/views.py

from django.shortcuts import render, redirect
from .mongo import todos_collection
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://hari_haran:12345@cluster0.sdva6.mongodb.net/')
db = client['todo_project']
todos_collection = db['todos']


def profile(request):
    return render(request, 'todo/profile.html')

def dashboard(request):
    return render(request, 'todo/dashboard.html')

def todo_list(request):
    todos = list(todos_collection.find())  # Fetch all to-do items
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todos_collection.insert_one({'title': title, 'completed': False})
        return redirect('todo_list')
    return render(request, 'todo/add_todo.html')

def about(request):
    return render(request, 'todo/about.html')