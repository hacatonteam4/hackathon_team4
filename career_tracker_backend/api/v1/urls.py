"""URL приложения API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    DirectionView,
    GetPlanStudent,
    GradeDirectionDescription
)

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('directions/', DirectionView.as_view()),
    path('description_direction/', GradeDirectionDescription.as_view()),
    path('plan/', GetPlanStudent.as_view()),
    path('', include(router.urls)),
    # path('map/', MapView.as_view()),
    # path('statistics/', StatisticView.as_view())
]
