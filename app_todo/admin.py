from django.contrib import admin

from app_todo.models import Todo, Tag

admin.site.register(Todo)
admin.site.register(Tag)
