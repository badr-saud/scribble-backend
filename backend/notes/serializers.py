from rest_framework import serializers

from .models import Note, Tag


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "text", "created_at", "updated_at", "user_id", "tag"]
        extra_kwargs = {"user_id": {"read_only": True}}


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "color"]
