from django import forms

from app_todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%d-%m-%Y %H:%M'),
        input_formats=('%d-%m-%Y %H:%M',)
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "done", "tags"]
