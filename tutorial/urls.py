from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from million import views
from rest_framework_simplejwt import views as jwt_views




urlpatterns = [
	path('table',views.TableView.as_view()),
    path('admin/', admin.site.urls),
    path('',include('million.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
