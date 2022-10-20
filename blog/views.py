from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    '''
    overriding perform_create cuz I was getting an "NOT NULL constraint failed: blog_post.author_id" error
    '''
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     print('here', kwargs)
    #     kwargs['author'] = self.request.user
    #     return self.create(request, *args, **kwargs)


    # def form_valid(self, form):     
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer