from django.test import TestCase, Client
from django.urls import reverse
from app_todo.models import Task, Tag


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("home")
        self.tag1 = Tag.objects.create(
            name="Tag 1",
        )
        self.todo1 = Task.objects.create(
            content="Todo 1",
            done=False,
        )
        self.todo1.tags.add(self.tag1)

    def test_todo_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_list.html")

    def test_todo_update(self):
        url = reverse("task_update", args=[str(self.todo1.id)])
        response = self.client.post(url, {
            "content": "Updated content",
            "done": True,
            "tags": self.tag1.id,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.first().content, "Updated content")

    def test_todo_delete(self):
        url = reverse("todo_delete", args=[str(self.todo1.id)])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_todo_complete(self):
        url = reverse("todo_complete", args=[str(self.todo1.id)])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.first().done, True)

    def test_todo_undo(self):
        url = reverse("todo_undo", args=[str(self.todo1.id)])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.first().done, False)
