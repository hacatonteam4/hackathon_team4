from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from specialties.models import (Specialization, Grade, Direction,
                                Course, GradeDirection, Skill)
from students.models import StudentCourse
from api.v1.serializers import GradeSerializer, SpecializationSerializer, MapSerializer, UserSerializer


class StatisticsView(APIView):

    def get(self, request):
        print(request)
        return Response(
            UserSerializer(request.user, context={'request': request}).data
        )


# class MapView(generics.ListAPIView):
#     serializer_class = MapSerializer
#     queryset = Skill.objects.all()
