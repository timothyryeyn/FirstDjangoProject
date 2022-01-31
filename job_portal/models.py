from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Seeker(models.Model):
    full_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    experience = models.TextField(default=None, blank=True, null=True)
    about_me = models.TextField(default=None, blank=True, null=True)
    resume = models.FileField(default=None, blank=True, null=True, upload_to='documents/%Y/%m/%d')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if (self.full_name is None): 
            return self.user.username

        return self.full_name


class Provider(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    about = models.TextField(default=None, blank=True, null=True)
    city = models.CharField(max_length=255, default=None, blank=True, null=True)
    country = models.CharField(max_length=255, default=None, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if (self.name is None): 
            return self.user.username
            
        return self.name


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

    def __str__(self):
        return self.name


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.name + "-" + self.seeker.full_name


class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SeekerSkill(models.Model):
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.seeker.full_name + "-" + self.skill.name


class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.job.name + "-" + self.skill.name
