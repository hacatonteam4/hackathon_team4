from rest_framework import serializers
from drf_base64.fields import Base64ImageField

from specialties.models import (Direction, Specialization,
                                Grade, GradeDirection, Skill)
from students.models import SkillStudent, StudentCourse, Student, StudentSpecialization


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


class SpecializationSerializer(serializers.ModelSerializer):
    '''Отображение специальности в статистике'''
    name = serializers.CharField(source='specialization.name')
    current_grade = GradeSerializer()

    class Meta:
        model = StudentSpecialization
        fields = ('id', 'name', 'current_grade')


class UserSerializer(serializers.ModelSerializer):
    specializations = SpecializationSerializer(
        many=True, source='students_specialization')

    class Meta:
        model = Student
        fields = ('id', 'username', 'specializations')


class MapSerializer(serializers.ModelSerializer):
    direction = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ('id', 'name', 'direction')

    def get_direction(self, obj):
        dicrection = Direction.objects.filter(
            grades_direction__skills=obj
        )
        return dicrection
