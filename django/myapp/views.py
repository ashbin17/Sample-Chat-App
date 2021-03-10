# Register API
from rest_framework import generics, permissions
from rest_framework import response
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage
from datetime import datetime


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#login
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.http import JsonResponse


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        user = serializer.validated_data['user']
        # user_serializer = UserSerializer(user)
        login(request, user)
        # return JsonResponse(user, safe=False)
        return super(LoginAPI, self).post(request, format=None)

#change password
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userdetails(request):
    if request.method == 'GET':
        user = request.user
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)


from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allusers(request):
    if request.method == 'GET':
        users = User.objects.filter(~Q(pk=request.user.pk)).order_by('username')
        user_serializer = UserSerializer(users, many=True)
        details = Customuser.objects.filter(~Q(user=request.user.pk))
        details_serializer = CustomSerializerA(details, many=True)
        return JsonResponse({'user_serializer':user_serializer.data, 'details_serializer': details_serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getuserdetails(request):
    try:
        details = Customuser.objects.get(user=request.user)
    except Customuser.DoesNotExist:
        return JsonResponse({'message': 'User detail is not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        details_serializer = CustomSerializer(details)
        return JsonResponse(details_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def adduserdetails(request):
    if request.method == 'POST':
        details_data = JSONParser().parse(request)
        detail_serializer = CustomSerializer(data=details_data)
        if detail_serializer.is_valid():
            detail = Customuser()
            detail.user = request.user
            detail.nickname = detail_serializer.data['nickname']
            detail.phone = detail_serializer.data['phone']
            detail.language = detail_serializer.data['language']
            detail.dob = detail_serializer.data['dob']
            detail.pic = detail_serializer.data['pic']
            detail.save()
            return JsonResponse(detail_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edituserdetails(request):
    if request.method == 'PUT':
        details_data = JSONParser().parse(request)
        detail = Customuser.objects.get(user=request.user)
        detail_serializer = CustomSerializer(detail, data=details_data)
        if detail_serializer.is_valid():
            detail_serializer.save()
            return JsonResponse(detail_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def savefile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request, text):
    if User.objects.filter(username__icontains=text).exists():
        users = User.objects.filter(~Q(pk=request.user.pk), username__icontains=text)
        users_serializer = UserSerializer(users, many=True)
        details = Customuser.objects.all()
        details_serializer = CustomSerializerA(details, many=True)
        return JsonResponse({'user_serializer': users_serializer.data, 'details_serializer': details_serializer.data})
    else:
        return JsonResponse({'message': 'search fail'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getforeignuser(request, id):
    users = User.objects.get(pk=id)
    users_serializer = UserSerializer(users)
    details = Customuser.objects.get(user=users)
    details_serializer = CustomSerializerA(details)
    return JsonResponse({'user_serializer': users_serializer.data, 'details_serializer': details_serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendmessage(request):
    data = JSONParser().parse(request)
    data_serializer = MessageSerializer(data=data)
    if data_serializer.is_valid():
        sender = User.objects.get(pk=data_serializer.data['sender'])
        receiver = User.objects.get(pk=data_serializer.data['receiver'])
        date = datetime.now()
        msg = Message()
        msg.sender = sender
        msg.receiver = receiver
        msg.msg = data_serializer.data['msg']
        msg.date = date
        msg.save()
        msg_serializer = MessageSerializerA(msg)
        return Response(msg_serializer.data)
    else:
        return JsonResponse({'message': 'fail'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_message(request, sender, receiver):
        sender = User.objects.get(pk=sender)
        receiver = User.objects.get(pk=receiver)
        if Message.objects.filter(Q(sender=sender, receiver=receiver) | Q(sender=receiver,receiver=sender)).exists():
            msg = Message.objects.filter(Q(sender=sender, receiver=receiver) | Q(sender=receiver,receiver=sender)).order_by('date')
            msg_serializer = MessageSerializerA(msg, many=True)
            return Response(msg_serializer.data)
        else:
            return JsonResponse({'message': 'fail'}, status=status.HTTP_400_BAD_REQUEST)
