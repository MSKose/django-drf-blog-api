from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
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
    overriding the perform_create method cuz I was getting a "NOT NULL constraint failed: blog_post.author_id" error
    '''
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET','POST'])
def like(request, pk):
    queryset = Like.objects.all()
    LikeSerializers = LikeSerializer(queryset, many=True)   
    
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs.exists():
                like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=post)
        return Response(LikeSerializers.data)
    return Response(LikeSerializers.data)