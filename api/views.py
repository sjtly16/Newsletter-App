from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from django.conf import settings
from knox.models import AuthToken

#login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = AuthToken.objects.create(user)[1]
            return Response({
                "error": False,
                "message": "success",
                "user": LoginUserSerializer(user, context=self.get_serializer_context()).data,
                "token": token
            })
        else:
            return Response({
                "error": True,
                "message": serializer.errors,
            }, status=status.HTTP__400_BAD_REQUEST)




class SendMailAPI(APIView):
    permission_classes = [AllowAny,]
    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = request.data['subject']
            html_content = request.data['content']
            recipents = request.data['recipents']
            email_count = len(recipents)

            if len(email_count)>50:
                batches = [recipents[i:i + 50] for i in range(0, email_count, 50)]
                for batch in batches:
                    msg = EmailMessage(subject, html_content,
                                    settings.EMAIL_HOST_USER, bcc=batch, fail_silently=False)
                    msg.content_subtype = "html"  # Main content is now text/html
                    email_response = msg.send()
                return Response({
                    "error":False,
                    "message": "Success",
                    "email_response": email_response,
                }, status=status.HTTP_200_OK)    

            else:
                msg = EmailMessage(subject, html_content,
                                settings.EMAIL_HOST_USER, bcc=recipents, fail_silently=False)
                msg.content_subtype = "html"  # Main content is now text/html
                email_response = msg.send()
                return Response({
                    "error": False,
                    "message": "Success",
                    "email_response": email_response,
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": True,
                "message": serializer.errors,
            }, status=status.HTTP__400_BAD_REQUEST)

    


            


