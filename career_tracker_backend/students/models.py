from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from prof_tests.models import Test
# from course.models import Course


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


Student = get_user_model()


class StudentTest(models.Model):
    """Связь студентов с тестами"""
    student = models.ForeignKey(
        Student,
        verbose_name='Студент',
        on_delete=models.CASCADE
    )
    test = models.ForeignKey(
        Test,
        verbose_name='Тест',
        on_delete=models.CASCADE
    )
    percentage = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        default=Decimal(0),
        validators=PERCENTAGE_VALIDATOR,
        verbose_name='Пройденный процент теста'
    )
    result = models.BooleanField(
        default=False,
        verbose_name='Статус теста'
    )

    class Meta:
        ordering = ('student',)
        verbose_name = 'Связь студента и теста'
        verbose_name_plural = 'Связь студентов и тестов'
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'test',),
                name='unique_student_test'
            )
        ]

    def __str__(self):
        return (f'Студент {self.student} прошел тест {self.test} '
                f'на {self.percentage}% с результатом {self.result}')


# class StudentCourse(models.Model):
#     """Связь студентов с курсами"""
#     student = models.ForeignKey(
#         Student,
#         verbose_name='Студент',
#         on_delete=models.CASCADE
#     )
#     # course = models.ForeignKey(
#     #     Course,
#     #     verbose_name='Курс',
#     #     on_delete=models.CASCADE
#     # )
#     purchased = models.BooleanField(
#         verbose_name='Статус покупки',
#         default=False
#     )

#     class Meta:
#         ordering = ('student',)

#     def __str__(self):
#         return f'студент {self.student} проходит курс {self.course}'
