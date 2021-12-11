"""Users serailazers"""

from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import users


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = (
            'email',
            'phone_number',
            'username'
        )


class UserLoginSerializer(serializers.Serializer):

    """Handle user login authentication"""

    username = serializers.CharField()
    password = serializers.CharField(min_length = 8, max_length=64)

    def validate(self, data):
        """Credentials validation"""

        print (data)
        user = authenticate(username = data["username"], password = data["password"])
        print (user)
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        self.context['user'] = user

        return data

    def create(self, data):
        return self.context["user"]
