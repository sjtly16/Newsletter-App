from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100, required=False, allow_blank=True)
    content = serializers.CharField(max_length=None, allow_blank=False)
    recipients = serializers.ListField(
        child = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    )


    
