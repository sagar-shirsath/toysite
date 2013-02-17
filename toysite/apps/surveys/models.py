from django.db import models
from django.contrib.auth.models import User

class Option(models.Model):
    title = models.CharField(max_length=1000)

class Question(models.Model):
    title = models.CharField(max_length=1000)
    options = models.ManyToManyField(Option)

class Survey(models.Model):
    title = models.CharField(max_length=30)
    questions = models.ManyToManyField(Question)
    created_by = models.ForeignKey(User)

class SurveyAnswer(models.Model):
    user = models.ForeignKey(User)
    survey = models.ForeignKey(Survey)
    question = models.ForeignKey(Question)
    option  = models.ForeignKey(Option)

class SurveyCompleted(models.Model):
    user = models.ForeignKey(User)
    survey = models.ForeignKey(Survey)
    is_completed = models.BooleanField(default=False)

