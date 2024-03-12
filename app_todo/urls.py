from django.urls import path

from app_todo.views import (HomeListView,
                            TagListView,
                            TaskCreateView,
                            TaskUpdateView,
                            TaskDeleteView,
                            TaskStatusUpdateView,
                            TagCreateView,
                            TagUpdateView,
                            TagDeleteView)


urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("todo/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task_update"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task_delete"),
    path("tasks/<int:pk>/status_update/",
         TaskStatusUpdateView.as_view(),
         name="task_status_update"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
