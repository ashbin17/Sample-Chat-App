from rest_framework import views
from .views import RegisterAPI, LoginAPI, ChangePasswordView
from django.urls import path, include
from knox import views as knox_views
from . import views as customviews

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/userdetails/', customviews.userdetails, name='userdetails'),
    path('api/allusers/', customviews.allusers, name='allusers'),
    path('api/getuserdetails/', customviews.getuserdetails, name='getuserdetails'),
    path('api/adduserdetails/', customviews.adduserdetails, name='adduserdetails'),
    path('api/edituserdetails/', customviews.edituserdetails, name='edituserdetails'),
    path('api/savefile/', customviews.savefile, name='savefile'),
    path('api/search/<str:text>', customviews.search, name='search'),
    path('api/getforeignuser/<int:id>', customviews.getforeignuser, name='getforeignuser'),
    path('api/sendmessage/', customviews.sendmessage, name='sendmessage'),
    path('api/viewmessage/<int:sender>/<int:receiver>', customviews.view_message, name='viewmessage'),
]