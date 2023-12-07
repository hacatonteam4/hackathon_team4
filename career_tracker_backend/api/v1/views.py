from django.contrib.auth import get_user_model
from rest_framework import generics
# from rest_framework.views import APIView

from .serializers import GetDirectionSerializer
from specialties.models import (
    Direction,
    Specialization
)


Student = get_user_model()


class DirectionView(generics.ListAPIView):
    '''Обработка запроса на получение направлений специализации студента'''

    serializer_class = GetDirectionSerializer

    def get_queryset(self):
        specialization_student = Specialization.objects.filter(
            specialization_students__student=self.request.user
        )
        return Direction.objects.filter(
            grades_direction__specialization__in=specialization_student
        )
        # return Direction.objects.filter(
        #     grades_direction__specialization__specialization_students__student=self.request.user
        # )
