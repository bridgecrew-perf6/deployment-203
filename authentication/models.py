from ipaddress import ip_address
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserLoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    created = models.DateTimeField(auto_now_add=True)
