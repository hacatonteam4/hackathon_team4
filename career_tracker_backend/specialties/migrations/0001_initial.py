# Generated by Django 3.2 on 2023-12-05 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название курса')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название грейда')),
            ],
            options={
                'verbose_name': 'Грейд',
                'verbose_name_plural': 'Грейды',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название специальности')),
                ('image', models.ImageField(blank=True, null=True, upload_to='specialties/')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название спринта')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprints_course', to='specialties.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Спринт',
                'verbose_name_plural': 'Спринты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название навыка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skills_direction', to='specialties.direction', verbose_name='Направление')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skills_grade', to='specialties.grade', verbose_name='Грейд')),
                ('sprint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skills_sprint', to='specialties.sprint', verbose_name='Спринт')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GradeDirectionSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialties.direction')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialties.grade')),
                ('skills', models.ManyToManyField(related_name='skill_groups', to='specialties.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade_specialization', to='specialties.specialization', verbose_name='Специальность'),
        ),
        migrations.AddField(
            model_name='direction',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='direction_specialization', to='specialties.specialization', verbose_name='Специальность'),
        ),
        migrations.AddField(
            model_name='course',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses_specialization', to='specialties.specialization', verbose_name='Специальность'),
        ),
        migrations.AddConstraint(
            model_name='skill',
            constraint=models.UniqueConstraint(fields=('name', 'direction'), name='unique_direction_skill'),
        ),
    ]
