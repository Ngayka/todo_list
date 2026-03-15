from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    hashtag = serializers.SerializerMethodField()
    class Meta:
        model = Tag
        fields = ["hashtag"]

    def get_hashtag(self, obj):
        return f"#{obj.name}"


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ["id", "content", "date_of_applying", "deadline", "tags"]
        read_only_fields = ('date_of_applying',)
