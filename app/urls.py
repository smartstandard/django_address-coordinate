from django.contrib import admin
from django.urls import path
from geolocation.views import address_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('address/', address_view, name='address'),
]