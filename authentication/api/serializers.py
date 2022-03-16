from tkinter.ttk import Style
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
    def save(self):
        Use