from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Newsletter

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


class EmailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Newsletter
        fields = [
            'id',
            'subject',
            'content',
            'recipients',
            'created_at',
            'updated_at',
        ]

    
