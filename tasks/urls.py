from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskToggleView

app_name = 'tasks'

urlpatterns = [
    path("", TaskListView.as_view(), name='task_list'),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path('<int:pk>/delete', TaskDeleteView.as_view(), name="task_delete"),
    path('<int:pk>/update', TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/toggle/", TaskToggleView.as_view(), name="task_toggle"),
]
