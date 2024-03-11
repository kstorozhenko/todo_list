from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from app_todo.models import Todo, Tag


class HomeListView(generic.ListView):
    model = Todo
    template_name = "todo_list.html"


class TodoCreateView(generic.CreateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["content", "deadline", "done", "tags"]
    success_url = reverse_lazy("home")


class TodoUpdateView(generic.UpdateView):
    model = Todo
    template_name = "todo_form.html"
    fields = ["content", "deadline", "done", "tags"]
    success_url = reverse_lazy("home")


class TodoDeleteView(generic.DeleteView):
    model = Todo
    template_name = "todo_confirm_delete.html"
    success_url = reverse_lazy("home")


class TodoCompleteView(generic.View):
    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=kwargs['pk'])
        todo.done = True
        todo.save()
        return redirect(reverse_lazy("home"))


class TodoUndoView(generic.View):
    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=kwargs['pk'])
        todo.done = False
        todo.save()
        return redirect(reverse_lazy("home"))


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "tag_form.html"
    fields = ["name"]
    success_url = reverse_lazy("tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "tag_form.html"
    fields = ["name"]
    success_url = reverse_lazy("tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tag_confirm_delete.html"
    success_url = reverse_lazy("tags")
