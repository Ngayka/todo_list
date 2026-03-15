from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Tag
from .serializers import TagSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("its_done", "-date_of_applying")
    serializer_class = TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
