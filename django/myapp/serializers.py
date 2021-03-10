from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        '''customuser = Customuser()
        customuser.nickname = validated_data['nickname']
        customuser.user = user
        customuser.language = validated_data['language']
        customuser.dob = validated_data['dob']
        customuser.gender = validated_data['gender']
        customuser.phone = validated_data['phone']
        if validated_data['pic']:
            customuser.pic = validated_data['pic']
        customuser.save()'''
        return user

# change password
from rest_framework import serializers
from django.contrib.auth.models import User


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ('id', 'nickname', 'phone', 'language', 'dob', 'pic')


class CustomSerializerA(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ('id', 'nickname', 'phone', 'language', 'dob', 'pic', 'user')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'msg')


class MessageSerializerA(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'msg', 'date', 'status')

