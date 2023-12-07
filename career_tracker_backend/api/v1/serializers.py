from rest_framework import serializers

from specialties.models import (
    Course,
    Grade,
    GradeDirection,
    Direction,
    Skill
)


class GetCoursesSprecialization(serializers.ModelSerializer):
    """Сериализатор для получения всех курсов по специальности студента"""

    class Meta:
        model = Course
        fields = ('id', 'name')


class GradeDirectionSerializator(serializers.ModelSerializer):
    """Сериализатор для направлений навыков в рамках конкретного грейда"""

    id = serializers.IntegerField(source='direction.id')
    name = serializers.ReadOnlyField(source='direction.name')
    color = serializers.ReadOnlyField(source='direction.color')

    class Meta:
        model = GradeDirection
        fields = ('id', 'name', 'color', 'description')


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


class GetDirectionSerializer(serializers.ModelSerializer):
    """Сериализатор для получения направлений специальности студента
    с процентным отображением знаний"""

    percent_direction = serializers.SerializerMethodField()

    class Meta:
        model = Direction
        fields = (
            'id',
            'name',
            'percent_direction'
        )

    def get_percent_direction(self, obj):
        """Вычисление % знаний студента в рамках конкретного направления"""
        request = self.context.get('request')
        direction_skills_count = Skill.objects.filter(
            grades_digrections__direction=obj
        ).count()
        student__dir_skills_count = Skill.objects.filter(
            grades_digrections__direction=obj,
            sprint_skills__students_sprint__student=request.user
        ).count()
        return int(student__dir_skills_count / direction_skills_count * 100)
