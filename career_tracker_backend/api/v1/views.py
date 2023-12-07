from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


from specialties.models import Specialization, Grade, Direction, Skill, Course
from api.v1.serializers import (SkillsSerializer, StatisticSerializer,
                                StatisticDirectionsSerializer, GetCoursesSprecialization, GetGradeDirectionDescriptionSerializator)


class StatisticsView(APIView):

    @swagger_auto_schema(responses={status.HTTP_200_OK: StatisticSerializer, })
    def get(self, request):
        return Response(
            StatisticSerializer(
                request.user, context={'request': request}
            ).data
        )


class DirectionsInStatisticsView(generics.ListAPIView):

    serializer_class = StatisticDirectionsSerializer

    def get_queryset(self):
        specialization = Specialization.objects.get(
            students_specialization__student=self.request.user
        )
        return set(Direction.objects.filter(
            grades_direction__specialization=specialization
            )
        )


class CompleteSkillsView(generics.ListAPIView):
    serializer_class = SkillsSerializer

    def get_queryset(self):
        grade = Grade.objects.get(
            students_specialization__student=self.request.user
        )
        skills = Skill.objects.filter(
            grades_directions__grade=grade,
            sprint_skills__students_sprint__student=self.request.user
        )
        return skills


class UnexploredSkillsView(generics.ListAPIView):
    serializer_class = SkillsSerializer

    def get_queryset(self):
        grade = Grade.objects.get(
            students_specialization__student=self.request.user
        )
        skills = Skill.objects.exclude(
            sprint_skills__students_sprint__student=self.request.user
        ).filter(grades_directions__grade=grade)
        return skills


class GetPlanStudent(generics.ListAPIView):
    '''Обработка запроса на получение курсов по специальности студента'''

    serializer_class = GetCoursesSprecialization

    def get_queryset(self):
        return Course.objects.filter(
            specialization__specialization_students__student=self.request.user
        )


class GradeDirectionDescription(generics.ListAPIView):
    """
    Обработка запроса на получение описания группы навыков,
    связанных с пересечением грейда и направления.
    Возвращает:
        JsonResponse: JSON-ответ, содержащий описания групп навыков.

    Пример использования:
        GET /api/v1/description_direction/

    Ответ:
        {
            "data": [
                {
                    "id": 1,
                    "name": "grade 1",
                    "direction": [
                        {
                            "id": 1,
                            "name": "Direction 1",
                            "color": "#6F78FF",
                            "description": "Description"
                        },
                        {
                            "id": 2,
                            "name": "Direction 2",
                            "color": "#FFFFFF",
                            "description": "Description 2"
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "grade 2",
                    "direction": [
                        {
                            "id": 1,
                            "name": "Direction 1",
                            "color": "#6F78FF",
                            "description": "Description"
                        }
                    ]
                }
            ]
        }
    """

    serializer_class = GetGradeDirectionDescriptionSerializator

    def get_queryset(self):
        specialization_student = Specialization.objects.filter(
            specialization_students__student=self.request.user
        )
        return Grade.objects.filter(
            directions_grade__specialization__in=specialization_student
        ).distinct()
