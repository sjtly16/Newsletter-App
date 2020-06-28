from django.contrib import admin
from django.urls import path, include
from newsletterapp import api
from api.view import ApiRoot
urlpatterns = [
    path('', ApiRoot.as_view(), name="root")
    path('admin/', admin.site.urls),
    path('api/', include(api.edpoints)),
    path('api/auth/', include('knox.urls')),
]
