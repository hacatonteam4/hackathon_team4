from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from specialties.models import Course, Specialization
from .serializers import GetCoursesSprecialization
# Create your views here.


class GetPlanStudent(generics.ListAPIView):
    '''Обработка запроса на получение курсов по специальности студента'''

    serializer_class = GetCoursesSprecialization
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        a = Course.objects.filter(
            specialization__courses_specialization__course_students__student=self.request.user
        )
        print(a)
        return Course.objects.filter(
            specialization__courses_specialization__course_students__student=self.request.user
        )
