from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%Y-%m-%d")
    date_joined = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "is_staff", "last_login", "is_superuser", "is_active", "date_joined"]



class ModifyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email"]