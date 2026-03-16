from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Task


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.all().order_by("its_done", "-date_of_applying")
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks:task_list")


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/task_update.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks:task_list")


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.its_done = not task.its_done
        task.save()
        return redirect("tasks:task_list")
