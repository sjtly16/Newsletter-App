from django.urls import path
from .views import SubscriberAPI, SubConfirm, SubDelete

urlpatterns = [
    path('auth/login', LoginAPI.as_view(), name="login"),
    path('subsriber/', SubscriberCreate.as_view(), name="sub-create"),
    path('', SubscriberList.as_view(), name="sub-list"),
    path('confirm/', SubConfirm, name="sub-confirm"),
    path('delete/', SubDelete, name="sub-del"),
]
