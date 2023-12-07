from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from students.models import (
    StudentCourse,
    StudentSpecialization,
    SprintStudent,
    Student
)


class StudentCourseInline(admin.TabularInline):
    model = StudentCourse
    extra = 1
    min_num = 1


# class SkillStudentInline(admin.TabularInline):
#     model = SkillStudent
#     extra = 1
#     min_num = 1


class StudentSpecializationInline(admin.TabularInline):
    model = StudentSpecialization
    extra = 1
    min_num = 1


class SprintStudentInline(admin.TabularInline):
    model = SprintStudent
    extra = 1
    min_num = 1


class StudentAdmin(UserAdmin):
    inlines = (
        StudentCourseInline,
        StudentSpecializationInline,
        SprintStudentInline
    )


admin.site.unregister(Student)
admin.site.register(Student, StudentAdmin)
