from django.urls import path
from .views import LoginAPI, SendMailAPI

urlpatterns = [
    path('auth/login', LoginAPI.as_view(), name="login"),
    path('send_email/' SendMailAPI.as_view(), name="email"),

]
