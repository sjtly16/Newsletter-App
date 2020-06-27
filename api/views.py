from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import SubscriberSerializer
from .models import Subscriber
import jwt
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class SubscriberAPI(generics.ListCreateAPIView):
    queryset = Subsriber.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = SubscriberSerializer(queryset, data=request.data)
        
        if serializer.is_valid():
            email = request.POST['email']
            token = jwt.encode({'subscriber': email }, key='secret', algorithm='HS256')
            subscriber = Subscriber(email=email, token=token)
            subscriber.save()
            message = Mail(
                from_email=settings.FROM_EMAIL,
                to_emails=email,
                subject='Newsletter Confirmation',
                html_content='Thank you for signing up for DSC KIET email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&token={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                       email,
                                                       token))
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            return Response({
                "error": False,
                "message": "success",
                "data": serializer.data,
                "email-response":[
                    response.status_code,
                    response.body,
                    response.headers, 
                ]
            }, status=status.HTTP_200_OK)
        
        else:
            return Response({
                "error": True,
                "message": serializer.errors,
            }, status=status.HTTP__400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = SubscriberSerializer(queryset, many=True)
        return Response({
            "error": False,
            "message": "list of all subscribers"
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
        
