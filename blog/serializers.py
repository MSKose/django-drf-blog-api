from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_image', 'total_likes')

    def get_total_likes(self, instance):
        return Like.objects.filter(post=instance).count()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body',)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"