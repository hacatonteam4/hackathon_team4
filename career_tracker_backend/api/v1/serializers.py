from rest_framework import serializers

from drf_base64.fields import Base64ImageField

from specialties.models import Direction, Grade, GradeDirection, Skill, Course
from students.models import Student, StudentSpecialization


class GradeSerializer(serializers.ModelSerializer):
    '''Отображение грейда и его процента в статистике'''

    percent_grade = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = ('id', 'name', 'percent_grade',)

    def get_percent_grade(self, obj):
        student = self.context.get('request').user
        grade_skills = Skill.objects.filter(
            grades_directions__grade=obj
        ).count()
        student_skills = Skill.objects.filter(
            grades_directions__grade=obj,
            sprint_skills__students_sprint__student=student
        ).count()
        return int(student_skills / grade_skills * 100)


class DirectionSkillSerializator(serializers.ModelSerializer):
    """Сериализатор для направлений в рамках конкретного навыка"""

    id = serializers.IntegerField(source='direction.id')
    name = serializers.ReadOnlyField(source='direction.name')
    color = serializers.ReadOnlyField(source='direction.color')

    class Meta:
        model = GradeDirection
        fields = ('id', 'name', 'color')


class SpecializationSerializer(serializers.ModelSerializer):
    '''Отображение специальности в статистике'''
    name = serializers.CharField(source='specialization.name')
    current_grade = GradeSerializer()
    image = Base64ImageField(source='specialization.image')

    class Meta:
        model = StudentSpecialization
        fields = ('id', 'name', 'current_grade', 'image',)


class StatisticSerializer(serializers.ModelSerializer):
    specializations = SpecializationSerializer(
        many=True, source='students_specialization'
    )

    class Meta:
        model = Student
        fields = ('specializations',)


class SkillsSerializer(serializers.ModelSerializer):
    direction = DirectionSkillSerializator(
        many=True,
        source='grades_directions'
    )

    class Meta:
        model = Skill
        fields = ('id', 'name', 'direction')


class StatisticDirectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direction
        fields = ('id', 'name', 'color')


class GetCoursesSprecialization(serializers.ModelSerializer):

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
    percent_direction = serializers.SerializerMethodField()

    class Meta:
        model = Direction
        fields = (
            'id',
            'name',
            'percent_direction'
        )

    def get_percent_direction(self, obj):
        request = self.context.get('request')
        direction_skills_count = Skill.objects.filter(
            grades_digrections__direction=obj
        ).count()
        student__dir_skills_count = Skill.objects.filter(
            grades_digrections__direction=obj,
            sprint_skills__students_sprint__student=request.user
        ).count()
        return int(student__dir_skills_count / direction_skills_count * 100)
