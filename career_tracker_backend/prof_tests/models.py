from django.db import models


class Questions(models.Model):
    text = models.TextField()
    answer = models.TextChoices


class Test(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название теста'
    )
