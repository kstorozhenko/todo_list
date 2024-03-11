from django.urls import path

from app_todo.views import (HomeListView,
                            TagListView,
                            TodoCreateView,
                            TodoUpdateView,
                            TodoDeleteView,
                            TodoCompleteView,
                            TodoUndoView,
                            TagCreateView,
                            TagUpdateView,
                            TagDeleteView)


urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("todo/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:pk>/update/",
         TodoUpdateView.as_view(),
         name="todo_update"),
    path("todo/<int:pk>/delete/",
         TodoDeleteView.as_view(),
         name="todo_delete"),
    path("todo/<int:pk>/complete/",
         TodoCompleteView.as_view(),
         name="todo_complete"),
    path("todo/<int:pk>/undo/", TodoUndoView.as_view(), name="todo_undo"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
