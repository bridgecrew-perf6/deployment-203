from authentication.models import UserLoginHistory
from rest_framework import serializers

class UserLogHistorySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserLoginHistory
        fields = (
            'id','user','ip_address', 'created'
        )
