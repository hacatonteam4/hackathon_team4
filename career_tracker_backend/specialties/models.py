from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model

from django.core.validators import MinValueValidator, MaxValueValidator


Student = get_user_model()

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
MAX_LENGHT = 200


class Specialization(models.Model):
    '''Модель специальности студента'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название специальности',
        unique=True
    )
    direction = models.ManyToManyField(
        'Direction',
        related_name='directions',
        verbose_name='Направление обучения'
    )
    progress = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        default=Decimal(0),
        validators=PERCENTAGE_VALIDATOR,
        verbose_name='Пройденный процент теста'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.name


class Course(models.Model):
    '''Модель курса специальности'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название курса',
        unique=True
    )
    description = models.TextField(verbose_name='Описание')
    specialization = models.ForeignKey(
        Specialization,
        on_delete=True,
        unique=True,
        related_name='courses_specialization',
        verbose_name='Специальность'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Grade(models.Model):
    '''Модель уровня знаний по специальности'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название грейда',
        unique=True
    )
    image = models.ImageField(upload_to='grades/')
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.SET_NULL,
        null=True,
        related_name='grade_specialization',
        verbose_name='Специальность'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Грейд'
        verbose_name_plural = 'Грейды'

    def __str__(self):
        return self.name


class Skill(models.Model):
    '''Модель навыка по специальности'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название навыка',
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Статус навыка'
    )
    description = models.TextField(verbose_name='Описание')
    direction = models.ForeignKey(
        'Direction',
        on_delete=models.SET_NULL,
        null=True,
        related_name='skills_direction',
        verbose_name='Направление'
    )
    grade = models.ForeignKey(
        'Grade',
        on_delete=models.SET_NULL,
        null=True,
        related_name='skills_grade',
        verbose_name='Группа'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'group',),
                name='unique_group_skill'
            )
        ]

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название'
    )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name


class Sprint(models.Model):
    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название спринта'
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Статус спринта'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='sprints_course',
        verbose_name='Курс'
    )
    skill = models.ManyToManyField(
        Skill,
        related_name='sprints_skill',
        verbose_name='Навык'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Спринт'
        verbose_name_plural = 'Спринты'

    def __str__(self):
        return self.name
