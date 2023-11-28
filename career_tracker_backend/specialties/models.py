from django.db import models
from django.contrib.auth import get_user_model


Student = get_user_model()


MAX_LENGHT = 200


class Specialization(models.Model):
    '''Модель специальности студента'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название специальности',
        unique=True
    )
    # на диаграмме не так, но мне кажется, что это будет удобнее
    grade = models.ManyToManyField(
        'Grade',
        related_name='grades',
        verbose_name='Грейд'
    )
    # на диаграмме так, думаю, похоже на правду
    direction = models.ManyToManyField(
        'Direction',
        related_name='directions',
        verbose_name='Направление обучения'
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
    specialization = models.ManyToManyField(
        Specialization,
        related_name='speciality',
        verbose_name='Специальность'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


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


class Grade(models.Model):
    '''Модель уровня знаний по специальности'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название грейда',
        unique=True
    )
    # Возможно, сделать один ко многим от group_skill к Grade
    group_skill = models.ManyToManyField(
        'SkillGroup',
        related_name='groups',
        verbose_name='Группа навыков'
    )
    image = models.ImageField(upload_to='grades/')

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
    description = models.TextField(verbose_name='Описание')
    direction = models.ForeignKey(
        'Direction',
        on_delete=models.SET_NULL,
        null=True,
        related_name='skills_direction',
        verbose_name='Направление'
    )
    group = models.ForeignKey(
        'SkillGroup',
        on_delete=models.SET_NULL,
        null=True,
        related_name='skills_group'
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


class SkillGroup(models.Model):
    '''Модель групп навыков грейда специальности'''

    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название',
    )
    description = models.TextField(verbose_name='Описание')
    # skill = models.ForeignKey(
    #     Skill,
    #     on_delete=models.CASCADE,
    #     related_name='skills_group'
    # )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Группа навыков'
        verbose_name_plural = 'Группы навыков'

    def __str__(self):
        return self.name


# переименовал, чтобы не было ассоциации с таблицей связей
class Direction(models.Model):
    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название'
    )
    # skill = models.ForeignKey(
    #     Skill,
    #     on_delete=models.CASCADE,
    #     related_name='skills_direct'
    # )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name


# Честно говоря, не понял, что это
class Sprint(models.Model):
    name = models.CharField(
        max_length=MAX_LENGHT,
        verbose_name='Название спринта'
    )
    status = models.BooleanField(
        default=False,
        verbose_name='статус спринта'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='sprints_course',
        verbose_name='Курс'
    )
    skill = models.ManyToManyField(
        Skill,
        related_name='sprints_skill'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Спринт'
        verbose_name_plural = 'Спринты'

    def __str__(self):
        return self.name
