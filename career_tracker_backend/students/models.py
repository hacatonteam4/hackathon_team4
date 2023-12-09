from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from prof_tests.models import Test
from specialties.models import (
    Course,
    Sprint,
    Skill,
    Specialization,
    Grade
)


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


Student = get_user_model()


class StudentSpecialization(models.Model):
    '''Связь студентов и грейдов'''
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='students_specialization'
    )
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name='students_specialization'
    )
    current_grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        related_name='students_specialization'
    )


class StudentTest(models.Model):
    '''Связь студентов с тестами'''

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


class StudentCourse(models.Model):
    """Связь студентов с курсами"""

    student = models.ForeignKey(
        Student,
        related_name='student_courses',
        verbose_name='Студент',
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        related_name='course_students',
        verbose_name='Курс',
        on_delete=models.CASCADE
    )
    status_payment = models.BooleanField(
        verbose_name='Статус покупки',
        default=False
    )

    class Meta:
        ordering = ('student',)
        verbose_name = 'Связь студента и курса'
        verbose_name_plural = 'Связь студентов и курсов'
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'course',),
                name='unique_student_course'
            )
        ]

    def __str__(self):
        return f'студент {self.student} проходит курс {self.course}'


class SkillStudent(models.Model):
    '''Модель связи навыка и студента'''

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='skills_student',
        verbose_name='Студент'
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='students_skill',
        verbose_name='Навык'
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Статус получения навыка'
    )

    class Meta:
        ordering = ('student',)
        verbose_name = 'Связь студента и навыка'
        verbose_name_plural = 'Связь студентов и навыков'

    def __str__(self):
        return f'Студент {self.student} изучил навык {self.skill}'


class SprintStudent(models.Model):
    '''Модель связи спринта и студента'''

    sprint = models.ForeignKey(
        Sprint,
        on_delete=models.CASCADE,
        related_name='students_sprint',
        verbose_name='Спринт'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='sprints_student',
        verbose_name='Студент'
    )

    class Meta:
        ordering = ('student',)
        verbose_name = 'Связь студента и спринта'
        verbose_name_plural = 'Связь студентов и спринтов'

    def __str__(self):
        return f'Студент {self.student} прошел спринт {self.sprint}'
