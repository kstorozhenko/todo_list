from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from app_todo.forms import TaskForm
from app_todo.models import Task, Tag


class HomeListView(generic.ListView):
    model = Task
    template_name = "task_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.order_by("done", "-created_at")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("home")


class TaskStatusUpdateView(generic.View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.done = not task.done
        task.save()
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
