from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    hashtag = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ["hashtag"]

    def get_hashtag(self, obj):
        return f"#{obj.name}"
