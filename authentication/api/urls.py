from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from rest_framework.response import Response
from rest_framework import status, mixins


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username=username, password=password)
            user.save()
        else:
            return render(request,'users/register.html',{'messages':"Password doesn't match"})

    return render(request, 'users/register.html', {'form': form})

class AuthJWTToken(ObtainAuthToken):
    
    def post(self, request):
        post_data = request.data
        username = post_data['username']
        password = post_data['password']
        if username:
            try:
                user = User.objects.get(username=username)
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
            statuspwd = user.check_password(password)
            if statuspwd:
                get_jwt_token = GetJWTToken(post_data)
                resp = get_jwt_token.get_token_util()
                return Response(json.loads(resp.text), status=resp.status_code)
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
                        "status": False,e 
                        "error": "Please Enter the Password",
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )