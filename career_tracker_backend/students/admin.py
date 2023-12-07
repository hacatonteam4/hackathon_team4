from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from students.models import (
    StudentCourse,
    StudentSpecialization,
    SprintStudent,
    SkillStudent,
    Student
)


class StudentCourseInline(admin.TabularInline):
    model = StudentCourse
    extra = 1
    min_num = 0


class SkillStudentInline(admin.TabularInline):
    model = SkillStudent
    extra = 1
    min_num = 1


class StudentSpecializationInline(admin.TabularInline):
    model = StudentSpecialization
    extra = 1
    min_num = 0


class SprintStudentInline(admin.TabularInline):
    model = SprintStudent
    extra = 1
    min_num = 0


class StudentSpecializationInline(admin.TabularInline):
    model = StudentSpecialization
    extra = 1
    min_num = 0


class StudentAdmin(UserAdmin):
    inlines = (StudentCourseInline, SkillStudentInline,
               SprintStudentInline, StudentSpecializationInline)


admin.site.unregister(Student)
admin.site.register(Student, StudentAdmin)
