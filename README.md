ToDo List

This project is a simple yet powerful Todo List application built with Django. It allows users to manage their tasks efficiently and effectively.

Models
The application has two main models:

Todo: This model represents a task. Each task has a content field that stores the task description, a created_at field that stores the time when the task was created, a deadline field for the task deadline, and a done field that indicates whether the task has been completed. Tasks can be associated with multiple tags, which are represented by the tags field.
Tag: This model represents a tag that can be associated with one or more tasks. Each tag has a name field.
Views
The application provides several views for interacting with the Todo and Tag models:

HomeListView: This view displays a list of tasks. The tasks are paginated, with 5 tasks per page.
TodoCreateView: This view allows users to create a new task.
TodoUpdateView: This view allows users to update an existing task.
TodoDeleteView: This view allows users to delete a task.
TodoCompleteView: This view allows users to mark a task as completed.
TodoUndoView: This view allows users to mark a completed task as not done.
TagListView: This view displays a list of all tags.
TagCreateView: This view allows users to create a new tag.
TagUpdateView: This view allows users to update an existing tag.
TagDeleteView: This view allows users to delete a tag.
Each view is associated with a template that defines how it should be rendered. The views use Django’s generic views system, which simplifies the process of creating views for common tasks.