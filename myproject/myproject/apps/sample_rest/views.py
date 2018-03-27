from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from .serializers.users import UserSerializer, UserListSerializer
from .models.users import User

# Create your views here.


@api_view(['GET', 'POST'])
def hello(request):
    """ Sample endpoint """

    return Response({'hello': 'world'})


@api_view(['GET'])
def users(request):
    """ Get all users """

    # User class
    u = User()

    # User List serializer
    serializer = UserListSerializer(data=u.getUsers())

    # Valid response
    if serializer.is_valid():
        return JsonResponse(serializer.data, status=201, safe=False)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def user(request, user_id):
    """ Get one user by ID """

    # User class
    u = User()

    # User serializer
    serializer = UserSerializer(data=u.getUser(user_id))

    # Valid response
    if serializer.is_valid():
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def parseJson(request):
    """ Get one user by ID (input as JSON) """

    # User class
    u = User()

    # Parse Json input
    data = JSONParser().parse(request)
    user_id = data['id']

    # User serializer
    serializer = UserSerializer(data=u.getUser(user_id))

    # Valid response
    if serializer.is_valid():
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)
