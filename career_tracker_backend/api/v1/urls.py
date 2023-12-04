"""URL приложения API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GetPlanStudent


app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('plan/', GetPlanStudent.as_view()),
    path('', include(router.urls))
]
