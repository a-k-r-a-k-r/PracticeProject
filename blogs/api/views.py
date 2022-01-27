from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Models
from django.contrib.auth.models import User
# Serializers
from .serializers import UserSerializer, ModifyUserSerializer, AddUserSerializer


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    user_serializer = UserSerializer(users, many=True)
    return Response(user_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_info(request, id):
    data = {}
    try:
        user_object = User.objects.get(pk=id)
    except User.DoesNotExist:
        data["result"] = "User Not Found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method =="GET":
        user_serializer = UserSerializer(user_object)
        data["result"] = "Success"
        data["object"] = user_serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def user_info_update(request, id):
    data = {}
    try:
        user_object = User.objects.get(pk=id)
    except User.DoesNotExist:
        data["result"] = "User Not Found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method =="PUT":
        user_serializer = ModifyUserSerializer(user_object, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            data["result"] = "Updated"
            data["object"] = user_serializer.data
            return Response(data=data, status=status.HTTP_200_OK)
        data["result"] = "Invaid Request"
        data["object"] = user_serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_add(request):
    data = {}
    if request.method == "POST":
        user_serializer = AddUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            data["result"] = "Success"
            return Response(data=data, status=status.HTTP_200_OK)
        data["result"] = "Invalid Request"
        data["object"] = user_serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def user_del(request, id):
    data = {}
    try:
        user_object = User.objects.get(pk=id)
    except User.DoesNotExist:
        data["result"] = "User Not Found"
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        user_object.delete()
        data["result"] = "User deleted"
        return Response(data=data, status=status.HTTP_200_OK)
    
