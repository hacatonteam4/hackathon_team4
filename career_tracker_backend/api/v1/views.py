from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from specialties.models import Specialization, Grade, Direction, Skill, Course
from api.v1.serializers import (
    SkillsSerializer,
    StatisticSerializer,
    StatisticDirectionsSerializer,
    GetCoursesSpecialization,
    GetGradeDirectionDescriptionSerializator,
    GetDirectionSerializer
)


class StatisticsView(APIView):
    'Обработка запроса на получение специальности и прогресса по грейду'

    @extend_schema(
        responses={status.HTTP_200_OK: StatisticSerializer},
        summary='''
        Отображение специальности, ее изображения и
        процента прохождения грейда
        ''',
        tags=['Статистика студента']
    )
    def get(self, request):
        return Response(
            StatisticSerializer(
                request.user, context={'request': request}
            ).data
        )


@extend_schema(
    summary='''
        Отображение направлений специальности,
        прогресса по ним и цвета
        ''',
    tags=['Статистика студента']
)
class DirectionsInStatisticsView(generics.ListAPIView):
    '''Обработка запроса на получение направлений в статистике'''

    serializer_class = StatisticDirectionsSerializer

    def get_queryset(self):
        specialization = Specialization.objects.get(
            students_specialization__student=self.request.user
        )
        return set(Direction.objects.filter(
            grades_direction__specialization=specialization
            )
        )


@extend_schema(
    summary='''
        Отображение изученных навыков
        ''',
    tags=['Карта навыков']
)
class CompleteSkillsView(generics.ListAPIView):
    '''Отображение изученных навыков'''

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


@extend_schema(
    summary='''
        Отображение навыков для изучения
        ''',
    tags=['Карта навыков']
)
class UnexploredSkillsView(generics.ListAPIView):
    '''Отображение неизученных навыков'''

    serializer_class = SkillsSerializer

    def get_queryset(self):
        grade = Grade.objects.get(
            students_specialization__student=self.request.user
        )
        skills = Skill.objects.exclude(
            sprint_skills__students_sprint__student=self.request.user
        ).filter(grades_directions__grade=grade)
        return skills


@extend_schema(
    summary='''
        Отображение всех курсов по специальности студента
        ''',
    tags=['План роста']
)
class GetPlanStudent(generics.ListAPIView):
    '''Обработка запроса на получение курсов по специальности студента'''

    serializer_class = GetCoursesSpecialization

    def get_queryset(self):
        return Course.objects.filter(
            specialization__students_specialization__student=self.request.user
        )


@extend_schema(
    summary='''
        Отображение процентов изучения направлений на диаграмме
        ''',
    tags=['План роста']
)
class DirectionView(generics.ListAPIView):
    '''Обработка запроса на получение направлений специализации студента'''

    serializer_class = GetDirectionSerializer

    def get_queryset(self):
        specialization_student = Specialization.objects.filter(
            students_specialization__student=self.request.user
        )
        return Direction.objects.filter(
            grades_direction__specialization__in=specialization_student
        ).distinct()


@extend_schema(
    summary='''
        Направления с описанием каждой группы направлений для грейда
        ''',
    tags=['Статистика студента']
)
class GradeDirectionDescription(generics.ListAPIView):
    '''
    Обработка запроса на получение описания группы навыков,
    связанных с пересечением грейда и направления.
    '''

    serializer_class = GetGradeDirectionDescriptionSerializator

    def get_queryset(self):
        specialization_student = Specialization.objects.filter(
            students_specialization__student=self.request.user
        )
        return Grade.objects.filter(
            directions_grade__specialization__in=specialization_student
        ).distinct()
