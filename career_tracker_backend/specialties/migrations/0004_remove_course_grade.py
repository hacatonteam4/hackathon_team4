# Generated by Django 3.2 on 2023-12-08 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0003_course_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='grade',
        ),
    ]
