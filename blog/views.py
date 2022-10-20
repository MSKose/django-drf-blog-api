from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    '''
    overriding perform_create cuz I was getting a "NOT NULL constraint failed: blog_post.author_id" error
    '''
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer