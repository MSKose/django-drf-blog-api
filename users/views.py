from requests import request
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegistrationSerializer, ProfileUpdateForm
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        token = Token.objects.get(user=user)
        data['token'] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class ProfileView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateForm
    # print('here', request)


    def get_queryset(self):
    #     # return self.queryset.filter(user=request.user.profile)
    #     # print('requested data', dir(request))
        print('requested data', self.kwargs['pk'])
    #     print(self.queryset.first().image.url)
    #     print(User.objects.all().first().user)
        return self.queryset.all()
    
    # def get(self, request, *args, **kwargs):
    #     print('here', self.request.profile)
    #     return self.retrieve(request, *args, **kwargs)

class OnlyRet(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateForm

    def get(self, request, *args, **kwargs):
        print(self.request)
        print(self.get_object())
        return self.retrieve(request, *args, **kwargs)