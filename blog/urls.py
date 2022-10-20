from django.urls import path, include
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('post', PostCRUD)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', PostListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/create/', PostCreateView.as_view(), name="post-create"),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name="post-update"),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="post-delete"),
]