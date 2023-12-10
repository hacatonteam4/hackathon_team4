"""URL приложения API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    StatisticsView,
    CompleteSkillsView,
    UnexploredSkillsView,
    DirectionsInStatisticsView,
    GetPlanStudent,
    GradeDirectionDescription,
    DirectionView
)


app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('complete_skills/', CompleteSkillsView.as_view()),
    path('unexplored_skills/', UnexploredSkillsView.as_view()),
    path('statistics/', StatisticsView.as_view()),
    path('statistics_directions/', DirectionsInStatisticsView.as_view()),
    path('plan/', GetPlanStudent.as_view()),
    path('description_direction/', GradeDirectionDescription.as_view()),
    path('directions/', DirectionView.as_view()),
    path('', include(router.urls)),
    # path('map/', MapView.as_view()),
    # path('statistics/', StatisticView.as_view())
]
