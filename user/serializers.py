from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "password")


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        user = User.objects.filter(email=attrs["email"]).first()
        if user and not user.is_active:
            raise AuthenticationFailed(
                "User account is not active, check your email to activate your account.",
                "no_active_account",
            )
        data = super().validate(attrs)

        return {"access": data["access"]}
