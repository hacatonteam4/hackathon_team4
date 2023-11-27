from django.db import models
from django.contrib.auth import get_user_model

Student = get_user_model()


MAX_LENGHT = 200


class Specialization(models.Model):
    '''Модель специальности студента'''

    name = models.CharField(max_length=MAX_LENGHT)
    grade = models.ForeignKey(
        'Grade',
        on_delete=models.CASCADE,
        related_name='grades'
    )
    direction = models.ForeignKey(
        'DirectionSpeciality',
        on_delete=models.CASCADE,
        related_name='directions'
    )


class Course(models.Model):
    '''Модель курса специальности'''

    name = models.CharField(max_length=MAX_LENGHT)
    description = models.TextField()
    specialization = models.ManyToManyField(
        Specialization,
        related_name='speciality'
    )


class StudentCourse(models.Model):
    """Связь студентов с курсами"""

    student = models.ForeignKey(
        Student,
        related_name='courses',
        verbose_name='Студент',
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        related_name='courses',
        verbose_name='Курс',
        on_delete=models.CASCADE
    )
    status_payment = models.BooleanField(
        verbose_name='Статус покупки',
        default=False
    )

    class Meta:
        ordering = ('student',)

    def __str__(self):
        return f'студент {self.student} проходит курс {self.course}'


class Grade(models.Model):
    '''Модель уровня знаний по специальности'''

    name = models.CharField(max_length=MAX_LENGHT)
    group_skill = models.ForeignKey(
        'SkillGroup',
        on_delete=models.CASCADE,
        related_name='groups'
    )
    # Поле для картинки


class Skill(models.Model):
    '''Модель навыка по специальности'''

    name = models.CharField(max_length=MAX_LENGHT)
    description = models.TextField()


class SkillGroup(models.Model):
    '''Модель групп навыков грейда специальности'''

    name = models.CharField(max_length=MAX_LENGHT)
    description = models.TextField()
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='skills_group'
    )


class DirectionSpeciality(models.Model):
    name = models.CharField(max_length=MAX_LENGHT)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='skills_direct'
    )
