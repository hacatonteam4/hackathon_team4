"""URL приложения API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.views import StatisticsView


app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('map/', MapView.as_view()),
    path('statistics/', StatisticsView.as_view())
]
