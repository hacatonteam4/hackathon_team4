"""URL приложения API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GradeDirectionDescription

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('description_direction/', GradeDirectionDescription.as_view()),
    path('', include(router.urls)),
    # path('map/', MapView.as_view()),
    # path('statistics/', StatisticView.as_view())
]
