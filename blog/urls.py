from django.urls import path, include
from .views import PostListView, PostCRUD


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostCRUD)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', PostListView.as_view(), name="home"),
]