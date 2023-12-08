# Generated by Django 3.2 on 2023-12-08 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradedirection',
            name='skills',
            field=models.ManyToManyField(related_name='grades_directions', to='specialties.Skill'),
        ),
        migrations.AlterField(
            model_name='gradedirection',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades_directions', to='specialties.specialization'),
        ),
    ]
