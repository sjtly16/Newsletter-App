from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100, required=False, allow_blank=True)
    content = serializers.CharField(max_length=None, allow_blank=False)
    recipients = serializers.ListField(
        recipient = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    )


    
