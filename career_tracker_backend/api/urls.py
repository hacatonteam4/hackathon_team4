"""URL-роутинг приложения API."""
from django.urls import path, include

from career_tracker_backend.urls import VERSION_API


urlpatterns = [
    path(f'v{VERSION_API}/', include(f'api.{VERSION_API}.urls')),
]
