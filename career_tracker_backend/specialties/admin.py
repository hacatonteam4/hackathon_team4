from django.contrib import admin

from .models import (
    Specialization, Course, Grade, Skill, Direction, Sprint, GradeDirection
)


class DirectionInline(admin.TabularInline):
    model = Specialization.direction.through
    extra = 1
    min_num = 1


class SkillsInline(admin.TabularInline):
    model = Skill
    extra = 1
    min_num = 1


class SprintInline(admin.TabularInline):
    model = Sprint
    extra = 1
    min_num = 1


class GradeDirectionInline(admin.TabularInline):
    model = GradeDirection
    extra = 1
    min_num = 1


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'display_directions', 'image')
    fields = ('name', 'image')
    list_editable = ('name', 'image')
    list_filter = ('name', 'direction')
    search_fields = ('name', 'direction')
    empty_value_display = '-пусто-'
    inlines = (DirectionInline,)

    @admin.display(description='Направления')
    def display_directions(self, obj):
        return ", ".join([direction.name for direction in obj.direction.all()])


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
    list_display = ('pk', 'name', 'specialization', 'display_directions')
    list_editable = ('name', 'specialization')
    list_filter = ('name', 'specialization')
    search_fields = ('name', 'specialization')
    inlines = (SkillsInline, GradeDirectionInline)

    @admin.display(description='Направления')
    def display_directions(self, obj):
        return ", ".join([direction.name for direction in obj.direction.all()])


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'display_specialization')
    list_editable = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    inlines = (DirectionInline, SkillsInline,)

    @admin.display(description='Специальности')
    def display_specialization(self, obj):
        return ", ".join(
            [specialties.name for specialties in obj.specialties.all()]
        )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'direction',
        'grade',
        'sprint'
    )
    list_editable = ('name', 'description', 'direction', 'grade', 'sprint')
    list_filter = ('name', 'direction', 'grade', 'sprint')
    search_fields = ('name', 'direction', 'grade', 'sprint')
    empty_value_display = '-пусто-'


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'course')
    list_editable = ('name', 'course')
    list_filter = ('name', 'course')
    search_fields = ('name', 'course')
    empty_value_display = '-пусто-'
    # inlines = (SkillsInline,)
