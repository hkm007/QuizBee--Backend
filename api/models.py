from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    createdOn = models.DateField(default = timezone.now)
    q1 = models.TextField(max_length=1000, blank=True)
    a1 = models.CharField(max_length=100, blank=True)
    q2 = models.TextField(max_length=1000, blank=True)
    a2 = models.CharField(max_length=100, blank=True)
    q3 = models.TextField(max_length=1000, blank=True)
    a3 = models.CharField(max_length=100, blank=True)
    q4 = models.TextField(max_length=1000, blank=True)
    a4 = models.CharField(max_length=100, blank=True)
    q5 = models.TextField(max_length=1000, blank=True)
    a5 = models.CharField(max_length=100, blank=True)
    q6 = models.TextField(max_length=1000, blank=True)
    a6 = models.CharField(max_length=100, blank=True)
    q7 = models.TextField(max_length=1000, blank=True)
    a7 = models.CharField(max_length=100, blank=True)
    q8 = models.TextField(max_length=1000, blank=True)
    a8 = models.CharField(max_length=100, blank=True)
    q9 = models.TextField(max_length=1000, blank=True)
    a9 = models.CharField(max_length=100, blank=True)
    q10 = models.TextField(max_length=1000, blank=True)
    a10 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name