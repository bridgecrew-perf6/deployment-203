"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from authentication.views import AuthJWTToken, RegisterUser, login_view,signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth_token/', AuthJWTToken.as_view({'post':'create'}), name='login_url'),
    path('authentication/create_user', RegisterUser.as_view({'post':'create'}), name='signup_url'),
    path('',login_view, name='login_view'),
    path('signup_view',signup_view, name='signup_view'),
    path('accounts/', include('allauth.urls')),


]
