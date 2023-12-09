from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from specialties.models import (Specialization, Grade, Direction,
                                Course, GradeDirection, Skill)
from students.models import StudentCourse, Student
from api.v1.serializers import (GradeSerializer, SpecializationSerializer,
                                CompleteSkillsSerializer, UserSerializer,)


class StatisticsView(APIView):

    def get(self, request):
        print(request)
        return Response(
            UserSerializer(request.user, context={'request': request}).data
        )


class CompleteSkillsView(generics.ListAPIView):
    serializer_class = CompleteSkillsSerializer

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
    serializer_class = CompleteSkillsSerializer

    def get_queryset(self):
        grade = Grade.objects.get(
            students_specialization__student=self.request.user
        )
        skills = Skill.objects.exclude(
            students_skill__student=self.request.user
        ).filter(grades_directions__grade=grade)
        print(skills)
        return skills
