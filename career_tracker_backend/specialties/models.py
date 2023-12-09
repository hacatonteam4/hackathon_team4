from django.db import models
from colorfield.fields import ColorField


MAX_LENGHT = 200


class Specialization(models.Model):
    '''Модель специальности студента'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название специальности',
        unique=True
    )
    # direction = models.ManyToManyField(
    #     'Direction',
    #     related_name='specialties',
    #     verbose_name='Направление обучения'
    # )
    image = models.ImageField(upload_to='specialties/', null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return f'Специальность: {self.name}'


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
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses_specialization',
        verbose_name='Специальность'
    )
    duration = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Продолжительность курса'
    )
    experience = models.BooleanField(
        default=False,
        verbose_name='С опытом'
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
    # specialization = models.ForeignKey(
    #     Specialization,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='grade_specialization',
    #     verbose_name='Специальность'
    # )
    # direction = models.ManyToManyField(
    #     'Direction',
    #     through='GradeDirection',
    #     verbose_name='Направление',
    # )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Грейд'
        verbose_name_plural = 'Грейды'

    def __str__(self):
        return self.name


class GradeDirection(models.Model):
    '''Модель связей грейда и направления'''
    skills = models.ManyToManyField(
        'Skill',
        related_name='grades_digrections'
    )
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name='grades_digrections'
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        related_name='directions_grade',
        verbose_name='Грейд'
    )
    direction = models.ForeignKey(
        'Direction',
        on_delete=models.CASCADE,
        related_name='grades_direction',
        verbose_name='Направление'
    )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ('grade', 'direction')
        verbose_name = 'Связь грейда и направления'
        verbose_name_plural = 'Связи грейдов и направлений'
        constraints = [
            models.UniqueConstraint(
                fields=['grade', 'direction'],
                name='unique_grade_direction'
            )
        ]

    def __str__(self):
        return (f'{self.direction} относится к грейду {self.grade}')


class Skill(models.Model):
    '''Модель навыка по специальности'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название навыка',
    )
    description = models.TextField(verbose_name='Описание')
    # direction = models.ForeignKey(
    #     'Direction',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='skills_direction',
    #     verbose_name='Направление'
    # )
    # grade = models.ForeignKey(
    #     'Grade',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='skills_grade',
    #     verbose_name='Грейд'
    # )
    # sprint = models.ForeignKey(
    #     'Sprint',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='skills_sprint',
    #     verbose_name='Спринт'
    # )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Direction(models.Model):
    '''Модель направления навыков специальности'''
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]
    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название'
    )
    color = ColorField(
        samples=COLOR_PALETTE,
        verbose_name='Цвет'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name


class Sprint(models.Model):
    '''Модель спринта'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название спринта'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='sprints_course',
        verbose_name='Курс'
    )
    skills = models.ManyToManyField(
        Skill,
        related_name='sprint_skills'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Спринт'
        verbose_name_plural = 'Спринты'

    def __str__(self):
        return self.name
