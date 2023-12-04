from rest_framework import generics

from specialties.models import Course
from .serializers import GetCoursesSprecialization
# Create your views here.


class GetPlanStudent(generics.ListAPIView):
    '''Обработка запроса на получение курсов по специальности студента'''

    serializer_class = GetCoursesSprecialization

    def get_queryset(self):
        return Course.objects.filter(
            specialization__courses_specialization__course_students__student=self.request.user
        )
