from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)


VERSION_API = '1'

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger'
    ),
    path(
        'api/redoc/', SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
