from rest_framework import serializers

from specialties.models import Grade, GradeDirection


class GradeDirectionSerializator(serializers.ModelSerializer):
    """Сериализатор для направлений навыков в рамках конкретного грейда"""

    id = serializers.IntegerField(source='direction.id')
    name = serializers.ReadOnlyField(source='direction.name')

    class Meta:
        model = GradeDirection
        fields = ('id', 'name', 'description')


class GetGradeDirectionDescriptionSerializator(serializers.ModelSerializer):
    """
    Сериализатор для ответа, содержащего описания групп навыков
    пересечения грейда и направления
    """

    direction = GradeDirectionSerializator(
        many=True,
        source='directions_grade'
    )

    class Meta:
        model = Grade
        fields = ('id', 'name', 'direction')
