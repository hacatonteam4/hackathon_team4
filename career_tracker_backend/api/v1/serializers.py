from rest_framework import serializers

from specialties.models import Direction, Skill


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
