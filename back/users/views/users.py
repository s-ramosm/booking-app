import re
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.serializers import UserLoginSerializer,UserModelSerializer

#Serializer 



class UsersLoginViews(APIView):

    def post(self, request,*args, **kwargs):
        """HTTP request post"""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        data = {
            "user" :  UserModelSerializer(user).data
        }

        return Response(data = data, status = status.HTTP_201_CREATED)
        
 