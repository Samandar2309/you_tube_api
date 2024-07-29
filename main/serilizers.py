from rest_framework import serializers
from authentication.models import CustomUser
from .models import Tag, Category, Video, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUser()
    video = VideoSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
