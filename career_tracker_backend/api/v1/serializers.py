from rest_framework import serializers
from drf_base64.fields import Base64ImageField

from specialties.models import (Direction, Specialization,
                                Grade, GradeDirection, Skill)
from students.models import (SkillStudent, StudentCourse,
                             Student, StudentSpecialization)


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
            students_skill__student=student
        ).count()
        return int(student_skills / grade_skills * 100)


# class GradeSerializer(serializers.ModelSerializer):
#     '''Отображение грейда и его процента в статистике'''

#     id = serializers.IntegerField(source='grade.id')
#     name = serializers.CharField(source='grade.name')
#     percent_grade = serializers.SerializerMethodField()

#     class Meta:
#         model = GradeDirection
#         fields = ('id', 'name', 'percent_grade',)

#     def get_percent_grade(self, obj):
#         student = self.context.get('request').user
#         grade_skills = Skill.objects.filter(
#             grades_directions__grade=obj
#         ).count()
#         student_skills = Skill.objects.filter(
#             grades_directions__grade=obj,
#             students_skill__student=student
#         ).count()
#         return int(student_skills / grade_skills * 100)


class DirectionSkillSerializator(serializers.ModelSerializer):
    """Сериализатор для направлений в рамках конкретного навыка"""

    id = serializers.IntegerField(source='direction.id')
    name = serializers.ReadOnlyField(source='direction.name')
    color = serializers.ReadOnlyField(source='direction.color')

    class Meta:
        model = GradeDirection
        fields = ('id', 'name', 'color')


# class DirectionsInSpecialization(serializers.ModelSerializer):

#     class Meta:
#         model = Direction
#         fields = ('id', 'name', 'color')


# class SpecializationSerializer(serializers.ModelSerializer):
#     grade = GradeSerializer(source='grades_directions.grade', many=True)

#     class Meta:
#         model = Specialization
#         fields = ('id', 'name', 'image', 'grade',)


# class SpecializationSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(source='specialization.id')
#     name = serializers.CharField(source='specialization.name')
#     image = Base64ImageField(source='specialization.image')
#     grade = GradeSerializer()
#     directions = DirectionsInSpecialization(many=True, source='grades_direction')

#     class Meta:
#         model = GradeDirection
#         fields = ('id', 'name', 'image', 'grade', 'directions')


# class DirectionSerializer(serializers.ModelSerializer):
#     directions = DirectionSkillSerializator(
#         many=True, source='grades_directions')

#     class Meta:
#         model = Specialization
#         fields = ('directions',)


class SpecializationSerializer(serializers.ModelSerializer):
    '''Отображение специальности в статистике'''
    name = serializers.CharField(source='specialization.name')
    current_grade = GradeSerializer()
    image = Base64ImageField(source='specialization.image')
    # directions = DirectionSerializer(
    #     source='specialization'
    # )

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
