from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Models
from django.contrib.auth.models import User
# Serializers
from .serializers import UserSerializer, ModifyUserSerializer, AddUserSerializer


@api_view(['GET', ])
def user_list(request):
    data = {}
    try:
        users = User.objects.all()
    except:
        data["status"] = status.HTTP_404_NOT_FOUND
        data["message"] = "Users model not found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        if users.count()<1:
            data["status"] = status.HTTP_200_OK
            data["message"] = "No users found"
            return Response(data=data, status=status.HTTP_200_OK)
        user_serializer = UserSerializer(users, many=True)
        data["status"] = status.HTTP_200_OK
        data["message"] = "Success"
        data["data"] = {"users":user_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        data["status"] = status.HTTP_405_METHOD_NOT_ALLOWED
        data["message"] = "Method not allowed"
        return Response(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', ])
def user_info(request, id):
    data = {}
    if not isinstance(id, int):
        data["status"] = status.HTTP_400_BAD_REQUEST
        data["message"] = "Bad Request"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_object = User.objects.get(pk=id)
    except User.DoesNotExist:
        data["status"] = status.HTTP_404_NOT_FOUND
        data["message"] = "User Not Found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        user_serializer = UserSerializer(user_object)
        data["status"] = status.HTTP_200_OK
        data["message"] = "Success"
        data["data"] = {"user":user_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        data["status"] = status.HTTP_405_METHOD_NOT_ALLOWED
        data["message"] = "Method not allowed"
        return Response(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT', ])
def user_info_update(request, id):
    data = {}
    if not isinstance(id, int):
        data["status"] = status.HTTP_400_BAD_REQUEST
        data["message"] = "Bad Request"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_object = User.objects.get(pk=id)
    except User.DoesNotExist:
        data["status"] = status.HTTP_404_NOT_FOUND
        data["message"] = "User Not Found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        user_serializer = ModifyUserSerializer(user_object, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            data["status"] = status.HTTP_200_OK
            data["message"] = "User updated"
            data["data"] = {"user" : user_serializer.data}
            return Response(data=data, status=status.HTTP_200_OK)
        data["status"] = status.HTTP_400_BAD_REQUEST
        data["message"] = "Invaid Request"
        data["data"] = {"error": user_serializer.errors}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data["status"] = status.HTTP_405_METHOD_NOT_ALLOWED
        data["message"] = "Method not allowed"
        return Response(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', ])
def user_add(request):
    data = {}
    if request.method == "POST":
        user_serializer = AddUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            data["status"] = status.HTTP_200_OK
            data["message"] = "User added"
            data["data"] = {"user" : user_serializer.data}
            return Response(data=data, status=status.HTTP_200_OK)
        data["status"] = status.HTTP_400_BAD_REQUEST
        data["message"] = "Bad Request"
        data["data"] = {"error": user_serializer.errors}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    else:
        data["status"] = status.HTTP_405_METHOD_NOT_ALLOWED
        data["message"] = "Method not allowed"
        return Response(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE', ])
def user_del(request, id):
    data = {}
    if not isinstance(id, int):
        data["status"] = status.HTTP_400_BAD_REQUEST
        data["message"] = "Bad Request"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_object = User.objects.get(pk=id)
    except User.DoesNotExist:
        data["status"] = status.HTTP_404_NOT_FOUND
        data["message"] = "User Not Found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        user_object.delete()
        data["status"] = status.HTTP_200_OK
        data["message"] = "User deleted"
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        data["status"] = status.HTTP_405_METHOD_NOT_ALLOWED
        data["message"] = "Method not allowed"
        return Response(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['DELETE', 'GET', 'POST', 'PUT'])
def custom404(request, exception=None):
    data = {}
    data["status"] = status.HTTP_404_NOT_FOUND
    data["message"] = "Endpoint not found"
    return Response(data=data, status=status.HTTP_404_NOT_FOUND)
