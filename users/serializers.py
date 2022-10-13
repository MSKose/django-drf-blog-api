# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from .models import Profile


class RegistrationSerializer(serializers.ModelSerializer):
		# since email field set to blank=True and doesn't validate for uniqueness in source code (User/AbstractUser Model) we're defining it again.
		# for UniqueValidator see: https://www.django-rest-framework.org/api-guide/validators/#uniquevalidator
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), # therefore, this makes sure our emails are unique
            message='This Email has been used.')] 
            )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password], # validators validates the password for the required standarts
        style={"input_type": "password"} # this one is not required but adding this will have this field appear as 'passwrod' on browser api 
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs): # validating if password and password2 match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data): # we are creating a user but we do not want to include password as is; hence, we do not include it in user
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password']) # therefore, we are creating the password with set_password to send the hashed form and not the string form
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user'
        )

class ProfileUpdateForm(serializers.ModelSerializer): 
    class Meta:
        model = Profile 
        fields = ['image'] 