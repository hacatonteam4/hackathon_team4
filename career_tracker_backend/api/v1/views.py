from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from specialties.models import (Specialization, Grade, Direction,
                                Course, GradeDirection, Skill)
from students.models import StudentCourse, Student
from api.v1.serializers import (GradeSerializer, SpecializationSerializer,
                                SkillsSerializer, StatisticSerializer,
                                StatisticDirectionsSerializer)


class StatisticsView(APIView):

    def get(self, request):
        print(request)
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
        print(Direction.objects.filter(
            grades_direction__specialization=specialization
        ))
        return set(Direction.objects.filter(
            grades_direction__specialization=specialization
            )
        )



# class StatisticsView(generics.ListAPIView):
#     serializer_class = SpecializationSerializer

#     def get_queryset(self):
#         specialization = Specialization.objects.get(
#             students_specialization__student=self.request.user
#         )
#         grade = Grade.objects.get(
#             students_specialization__student=self.request.user,
#             students_specialization__specialization=specialization
#         )
#         return GradeDirection.objects.filter(
#             specialization=specialization,
#             grade=grade
#         )


# class StatisticsView(generics.ListAPIView):
#     serializer_class = SpecializationSerializer

#     def get_queryset(self):

#         print('aaaaaaaaaaaaaaaaaaaaaa', Specialization.objects.filter(
#             students_specialization__student=self.request.user
#         ))

#         return Specialization.objects.filter(
#             students_specialization__student=self.request.user
#         )


class CompleteSkillsView(generics.ListAPIView):
    serializer_class = SkillsSerializer

    def get_queryset(self):
        grade = Grade.objects.get(
            students_specialization__student=self.request.user
        )
        skills = Skill.objects.filter(
            grades_directions__grade=grade,
            students_skill__student=self.request.user
        )
        return skills


class UnexploredSkillsView(generics.ListAPIView):
    serializer_class = SkillsSerializer

    def get_queryset(self):
        grade = Grade.objects.get(
            students_specialization__student=self.request.user
        )
        skills = Skill.objects.exclude(
            students_skill__student=self.request.user
        ).filter(grades_directions__grade=grade)
        print(skills)
        return skills
