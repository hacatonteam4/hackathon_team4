from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from .models import (
    Specialization, Course, Grade, Skill, Direction, Sprint, GradeDirection
)


# class DirectionInline(admin.TabularInline):
#     model = Specialization.direction.through
#     extra = 1
#     min_num = 1


# class SkillsInline(admin.TabularInline):
#     model = Skill
#     extra = 1
#     min_num = 1


class SprintInline(admin.TabularInline):
    model = Sprint
    extra = 1
    min_num = 0
    filter_horizontal = ('skills',)


class GradeDirectionInline(admin.TabularInline):
    model = GradeDirection
    extra = 0
    min_num = 0


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pk', 'name', 'image')
    fields = ('name', 'image')
    list_editable = ('name', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    inlines = (GradeDirectionInline,)

    # @admin.display(description='Направления')
    # def display_directions(self, obj):
    #     return ", ".join(
    #         [direction.name for direction in obj.direction.all()]
    #     )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'specialization')
    list_editable = ('name', 'description', 'specialization')
    list_filter = ('name', 'specialization')
    search_fields = ('name', 'specialization')
    empty_value_display = '-пусто-'
    inlines = (SprintInline,)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_editable = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_editable = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    # inlines = (DirectionInline,)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
    )
    list_editable = ('name', 'description',)
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'course')
    list_editable = ('name', 'course')
    list_filter = ('name', 'course')
    search_fields = ('name', 'course')
    empty_value_display = '-пусто-'
