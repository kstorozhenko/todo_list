from django.shortcuts import render
from django.views import generic

from app_todo.models import Todo


class HomeListView(generic.ListView):
    model = Todo
    template_name = "todo_list.html"

