from django.contrib import admin
from django.urls import path, include
from api.views import ApiRoot
from api import endpoints
urlpatterns = [
    path('', ApiRoot.as_view(), name="root"),
    path('admin/', admin.site.urls),
    path('api/', include(endpoints)),
    path('api/auth/', include('knox.urls')),
]
