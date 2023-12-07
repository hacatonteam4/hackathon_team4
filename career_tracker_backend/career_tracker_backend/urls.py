from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


VERSION_API = '1'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('api/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
