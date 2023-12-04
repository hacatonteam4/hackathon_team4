from django.contrib import admin

from .models import (
    Specialization, Course, Grade, Skill, Direction, Sprint
)


class DirectionInline(admin.TabularInline):
    model = Specialization.direction.through
    extra = 1
    min_num = 1


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'display_directions')
    fields = ('name',)
    list_editable = ('name',)
    list_filter = ('name', 'direction')
    search_fields = ('name', 'direction')
    empty_value_display = '-пусто-'
    # inlines = (DirectionInline,)

    @admin.display(description='Направления')
    def display_directions(self, obj):
        return ", ".join([direction.name for direction in obj.direction.all()])


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'specialization')
    list_editable = ('name', 'description', 'specialization')
    list_filter = ('name', 'description', 'specialization')
    search_fields = ('name', 'description', 'specialization')
    empty_value_display = '-пусто-'


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'specialization')
    list_editable = ('name', 'specialization')
    list_filter = ('name', 'specialization')
    search_fields = ('name', 'specialization')


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'display_specialization')
    list_editable = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    empty_value_display = '-пусто-'
    inlines = (DirectionInline,)

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
    list_filter = ('name', 'description', 'direction', 'grade', 'sprint')
    search_fields = ('name', 'description', 'direction', 'grade', 'sprint')
    empty_value_display = '-пусто-'


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'course')
    list_editable = ('name', 'course')
    list_filter = ('name', 'course')
    search_fields = ('name', 'course')
    empty_value_display = '-пусто-'
