from django.contrib import admin
from django.urls import path, include
from newsletterapp import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.edpoints)),
    path('api/auth/', include('knox.urls')),
]
