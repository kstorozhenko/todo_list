from django.test import TestCase

from app_todo.models import Tag, Todo


class TestModels(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="TestTAG")
        self.assertEqual(str(tag), tag.name)

    def test_todo_str(self):
        todo = Todo.objects.create(content="TestTODO")
        self.assertEqual(str(todo), todo.content)
