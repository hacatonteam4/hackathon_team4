from rest_framework import generics

from .serializers import GetGradeDirectionDescriptionSerializator
from specialties.models import (
    Grade,
    Specialization
)


class GradeDirectionDescription(generics.ListAPIView):
    """
    Обработка запроса на получение описания группы навыков,
    связанных с пересечением грейда и направления.
    Возвращает:
        JsonResponse: JSON-ответ, содержащий описания групп навыков.

    Пример использования:
        GET /api/v1/description_direction/

    Ответ:
        {
            "data": [
                {
                    "id": 1,
                    "name": "grade 1",
                    "direction": [
                        {
                            "id": 1,
                            "name": "Direction 1",
                            "color": "#6F78FF",
                            "description": "Description"
                        },
                        {
                            "id": 2,
                            "name": "Direction 2",
                            "color": "#FFFFFF",
                            "description": "Description 2"
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "grade 2",
                    "direction": [
                        {
                            "id": 1,
                            "name": "Direction 1",
                            "color": "#6F78FF",
                            "description": "Description"
                        }
                    ]
                }
            ]
        }
    """

    serializer_class = GetGradeDirectionDescriptionSerializator

    def get_queryset(self):
        specialization_student = Specialization.objects.filter(
            specialization_students__student=self.request.user
        )
        return Grade.objects.filter(
            directions_grade__specialization__in=specialization_student
        ).distinct()
