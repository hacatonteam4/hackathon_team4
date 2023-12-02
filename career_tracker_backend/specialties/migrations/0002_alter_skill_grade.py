# Generated by Django 3.2 on 2023-12-02 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skills_grade', to='specialties.grade', verbose_name='Грейд'),
        ),
    ]
