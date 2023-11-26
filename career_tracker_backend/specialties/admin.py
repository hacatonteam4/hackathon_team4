from django.contrib import admin

from .models import (
    Specialization, Course, Grade, SkillGroup, Skill, DirectionSpeciality
)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DirectionSpeciality)
class DirectionSpecialityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SkillGroup)
class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
