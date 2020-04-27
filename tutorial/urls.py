from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from million import views
#from million.views import home
from django.conf.urls import url
from tutorial import views as core_views

urlpatterns = [
#	path('',views.home, name='home'),
	path('signup/',views.signup, name='signup'),
	path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',include('million.urls')),
#    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
#   url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#        core_views.activate, name='activate')
]
