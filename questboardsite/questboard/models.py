from django.db import models
from django.urls import reverse


class Questboard(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    required_stars = models.IntegerField()


class Quest(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    star_count = models.IntegerField()
    student_1 = models.CharField(
        null=True, blank=True,
        max_length=100
    )
    student_2 = models.CharField(
        null=True, blank=True,
        max_length=100
    )
    student_3 = models.CharField(
        null=True, blank=True,
        max_length=100
    )
    is_for_everyone = models.BooleanField()
    questboard = models.ForeignKey(
        Questboard,
        on_delete=models.CASCADE,
        related_name='quests'
    )
