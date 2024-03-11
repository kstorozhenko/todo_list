from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from app_todo.models import Todo, Tag


class HomeListView(generic.ListView):
    model = Todo
    template_name = "todo_list.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag_list.html"


class TodoCreateView(generic.CreateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["content", "created_at", "deadline", "done", "tags"]


class TodoUpdateView(generic.UpdateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["content", "created_at", "deadline", "done", "tags"]


class TodoDeleteView(generic.DeleteView):
    model = Todo
    template_name = "todo_confirm_delete.html"
    success_url = reverse_lazy("home")



