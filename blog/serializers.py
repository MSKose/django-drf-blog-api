from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_image',)

    # def create(self, validated_data):
    #     print('here', validated_data)
    #     print('here2', self)
    #     user_author = validated_data.pop('author')
    #     instance = Post.objects.create(**validated_data)
    #     instance.user_author = user_author
    #     instance.save()
    #     return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body',)