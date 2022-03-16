from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from authentication.models import UserLoginHistory
from datetime import datetime
import requests

# def Register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         if password == confirm_password:
#             user = User.objects.create(username=username, password=password)
#             user.save()
#         else:
#             return render(request,'users/register.html',{'messages':"Password doesn't match"})

#     return render(request, 'users/register.html', {'form': form})

class RegisterUser(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        self.request = request
        post_data = self.request.data
        username = post_data['username']
        password = post_data['password']
        if not username:
            return Response(
                    {
                        "status": False,
                        "error": "Please Enter the Username",
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        if not password:
            return Response(
                    {
                        "status": False,
                        "error": "Please Enter the Password",
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        user = User.objects.create_user(username,password)
        user.save()
        return Response({'message':"user has been created successfully"} ,status=status=status.HTTP_200_OK)


            

class AuthJWTToken(viewsets.ModelViewSet):
    def send_webhook(self):
        self.ip_address = self.request.META.get('REMOTE_ADDR')
        headers = {'Content-type': 'application/json'}
        url = 'https://encrusxqoan0b.x.pipedream.net/'
        body = {"user": self.user.id, "ip": self.ip_address}
        webhook = requests.post(url, data = body)

    def create(self, request, *args, **kwargs):
        self.request = request
        post_data = self.request.data
        username = post_data['username']
        password = post_data['password']
        if username:
            try:
                self.user = User.objects.get(username=username)
            except:
                return Response(
                    {"error": "Invalid username"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    {
                        "status": False,
                        "error": "Please Enter the Username",
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        if password:
            statuspwd = self.user.check_password(password)
            if statuspwd:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(request.user)
                token = jwt_encode_handler(payload)
                self.send_webhook()
                userlog = UserLoginHistory.objects.create(user=self.user, ip_address = self.ip_address, created=datetime.now())
                userlog.save()
                return Response({'username':username, 'token':token}, status=status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "status": False,
                        "error": "Invalid Password",
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    {
                        "status": False,
                        "error": "Please Enter the Password",
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )