from django.urls import path, include

from app_todo.views import HomeListView

urlpatterns = [
    path("", HomeListView.as_view(), name="home")

]
