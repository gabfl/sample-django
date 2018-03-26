from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .serializers.users import UserSerializer, UserListSerializer
from .models.users import User

# Create your views here.


@api_view(['GET', 'POST'])
def hello(request):
    return Response({'hello': 'world'})


@api_view(['GET'])
def users(request):
    u = User()

    serializer = UserListSerializer(data=u.getUsers())

    if serializer.is_valid():
        # safe=False allows to return a list
        return JsonResponse(serializer.data, status=201, safe=False)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def user(request, user_id):
    u = User()

    serializer = UserSerializer(data=u.getUser(user_id))

    if serializer.is_valid():
        # serializer.save()
        # print(serializer.data)
        # print(serializer.is_valid())

        return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)
