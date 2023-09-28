from django.contrib import admin
from django.urls import path, include
from app.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register')
]
