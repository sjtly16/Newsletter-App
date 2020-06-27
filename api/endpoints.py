from django.urls import path
from .views import SubscriberAPI, Confirm, Delete

urlpatterns = [
    path('subsriber/', SubscriberCreate.as_view(), name="sub-create"),
    path('', SubscriberList.as_view(), name="sub-list"),
    path('confirm/', Confirm, name="sub-confirm"),
    path('delete/', Delete, name="sub-del"),
]
