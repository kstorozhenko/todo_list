from django import forms

from app_todo.models import Tag, Todo


class TodoForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Todo
        fields = ["content", "deadline", "done", "tags"]
