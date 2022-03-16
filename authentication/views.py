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
from authentication.serializers import UserLogHistorySerializer
from datetime import datetime
import requests
from django.contrib.auth import authenticate, login



class RegisterUser(viewsets.ModelViewSet):
    template_name = 'templates/signup.html'
    serializer_class = UserLogHistorySerializer

    def create(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
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
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({"message": 'User created successfully'},status=status.HTTP_200_OK)


            

class AuthJWTToken(viewsets.ModelViewSet):
    template_name = 'templates/login.html'
    serializer_class = UserLogHistorySerializer
    def send_webhook(self):
        self.ip_address = self.request.META.get('REMOTE_ADDR')
        headers = {'Content-type': 'application/json'}
        url = 'https://encrusxqoan0b.x.pipedream.net/'
        body = {"user": self.user.id, "ip": self.ip_address}
        webhook = requests.post(url, data = body)

    def create(self, request, *args, **kwargs):
        self.request = request
        post_data = self.request.data
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

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
            # hashed_password = make_password(password)
            # statuspwd = check_password(self.user.password, hashed_password)
            user = authenticate(username=username, password=password)
            if user:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(request.user)
                token = jwt_encode_handler(payload)
                self.send_webhook()
                userlog = UserLoginHistory.objects.create(user=self.user, ip_address = self.ip_address, created=datetime.now())
                userlog.save()
                return Response({'username':username, 'token':token},status=status.HTTP_200_OK)
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


def login_view(request):
    return render(request,'login.html',{})

def signup_view(request):
    return render(request,'signup.html',{})