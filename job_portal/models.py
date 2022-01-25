from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Seeker(models.Model):
    full_name = models.CharField(max_length=255)
    experience = models.TextField()
    about_me = models.TextField()
    resume_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Provider(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Job(models.Model):

    class Type(models.IntegerChoices):
        FULL_TIME = 1
        PART_TIME = 2

    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    type = models.IntegerField(choices=Type.choices)
    date_posted = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(Provider, on_delete=models.CASCADE)


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.CharField(max_length=255)


class SeekerSkill(models.Model):
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

