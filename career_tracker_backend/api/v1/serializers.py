from rest_framework import serializers

from drf_base64.fields import Base64ImageField

from specialties.models import (
    Course,
    Grade,
    GradeDirection,
    Direction,
    Skill,
    Sprint,
)
from students.models import Student, StudentSpecialization


class GradeSerializer(serializers.ModelSerializer):
    '''Получение грейда и его процента в статистике'''

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


class GradeDirectionSerializator(serializers.ModelSerializer):
    """Сериализатор для направлений навыков в рамках конкретного грейда"""

    id = serializers.IntegerField(source='direction.id')
    name = serializers.ReadOnlyField(source='direction.name')
    color = serializers.ReadOnlyField(source='direction.color')

    class Meta:
        model = GradeDirection
        fields = ('id', 'name', 'color', 'description')


class DirectionSkillSerializator(GradeDirectionSerializator):
    """Сериализатор для направлений в рамках конкретного навыка"""

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
    '''Отображение статистики по специальности и грейду'''

    specializations = SpecializationSerializer(
        many=True, source='students_specialization'
    )

    class Meta:
        model = Student
        fields = ('specializations',)


class SkillsSerializer(serializers.ModelSerializer):
    '''Получение навыков в карте навыков'''

    direction = DirectionSkillSerializator(
        many=True,
        source='grades_directions'
    )

    class Meta:
        model = Skill
        fields = ('id', 'name', 'description', 'direction')


class GetCoursesSpecialization(serializers.ModelSerializer):
    """Сериализатор для получения всех курсов по специальности студента"""

    progress = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'progress', 'duration', 'experience')

    def get_progress(self, obj):
        """Вычисление % прогресса по курсу у студента"""
        request = self.context.get('request')
        sprints_course = Sprint.objects.filter(
            course=obj
        ).count()
        sprints_student = Sprint.objects.filter(
            course=obj,
            students_sprint__student=request.user
        ).count()
        if sprints_course == 0:  # Для тестов, чтобы не добавлять спринты ко всем курсам
            return 0
        return int(sprints_student / sprints_course * 100)


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
            grades_directions__direction=obj
        ).count()
        student__dir_skills_count = Skill.objects.filter(
            grades_directions__direction=obj,
            sprint_skills__students_sprint__student=request.user
        ).count()
        return int(student__dir_skills_count / direction_skills_count * 100)


class StatisticDirectionsSerializer(GetDirectionSerializer):
    ''' Получение направлений с процентами прогресса и цветом в статистике'''

    class Meta:
        model = Direction
        fields = ('id', 'name', 'color', 'percent_direction')
