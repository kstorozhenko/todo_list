from django.urls import path

from app_todo.views import HomeListView, TagListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("todo/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:pk>/update/", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
]
