from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from million import views
from rest_framework_simplejwt import views as jwt_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('million.urls')),
	path('auth/',include('djoser.urls')),   
    path('auth/',include('djoser.urls.jwt')),


]
