# Generated by Django 3.2 on 2023-12-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]
