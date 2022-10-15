from django.urls import path, include
from .views import RegisterView, ProfileView, OnlyRet

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profiles/<int:pk>/', OnlyRet.as_view(), name='profile'),
]