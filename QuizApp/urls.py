from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls', namespace='myApp')),
    # Allows a POST request only
    path('auth/', obtain_auth_token),
]
