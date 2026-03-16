from rest_framework import serializers
from .models import Task
from tags.serializers import TagSerializer


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["id", "content", "date_of_applying", "deadline", "tags"]
        read_only_fields = ("date_of_applying",)
