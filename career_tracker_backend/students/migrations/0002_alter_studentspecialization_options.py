# Generated by Django 3.2 on 2023-12-10 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentspecialization',
            options={'ordering': ('student',), 'verbose_name': 'Связь студента специальности и грейда', 'verbose_name_plural': 'Связи студентов специальностей и грейдов'},
        ),
    ]