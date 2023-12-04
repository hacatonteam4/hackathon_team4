from rest_framework import serializers

from specialties.models import Course


class GetCoursesSprecialization(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name')
