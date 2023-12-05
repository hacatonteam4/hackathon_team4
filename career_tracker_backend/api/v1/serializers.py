from rest_framework import serializers

from specialties.models import Direction, Specialization, Grade


class StatisticsSerializer(serializers.ModelSerializer)