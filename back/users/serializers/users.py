"""Users serailazers"""

from django.db.models import fields
from rest_framework import serializers, validators
from django.contrib.auth import authenticate
from users.models import users


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = (
            'username',
            'email',
            'created',
            'phone_number',
        )


class UserLoginSerializer(serializers.Serializer):

    """Handle user login authentication"""

    username = serializers.CharField()
    password = serializers.CharField(min_length = 8, max_length=64)

    def validate(self, data):
        """Credentials validation"""
        user = authenticate(username = data["username"], password = data["password"])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet')

        self.context['user'] = user

        return data

    def create(self, data):
        return self.context["user"]


class UserSingUpSerializer(serializers.Serializer):

    phone_number = serializers.CharField(max_length=20)

    username = serializers.CharField(
        validators = [validators.UniqueValidator(queryset = users.objects.all())]
    )
    
    email = serializers.EmailField(
        validators = [validators.UniqueValidator(queryset = users.objects.all())]
    )
    
    
    # photo = serializers.ImageField(upload_to="user/pictures")

    password = serializers.CharField(
        min_length= 8,
        max_length=12
    )

    password_confirmation = serializers.CharField(
        min_length= 8,
        max_length=12
    )


    def validate(self, data):
        password =  data["password"]
        password_conf =  data["password_confirmation"]

        if password != password_conf:
            raise serializers.ValidationError("Passwords don't match.")

        return data

    def create(self, data):
        data.pop("password_confirmation")
        user = users.objects.create_user(**data)

        return user



