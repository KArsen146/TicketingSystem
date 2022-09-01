from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = '__all__'
