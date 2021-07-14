from rest_framework import serializers


class LoginSocialSerializer(serializers.Serializer):
    toke_id = serializers.CharField(required=True)
