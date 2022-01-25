from django.db import models


class Seeker(models.Model):
    title = models.CharField(max_length=100)
