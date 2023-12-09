"""URL приложения API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.views import (StatisticsView, CompleteSkillsView,
                          UnexploredSkillsView)


app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('complete_skills/', CompleteSkillsView.as_view()),
    path('unexplored_skills/', UnexploredSkillsView.as_view()),
    path('statistics/', StatisticsView.as_view())
]
