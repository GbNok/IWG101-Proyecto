from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Problem(models.Model):
    statement = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.statement

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution_file = models.FileField()   
    user = models.ForeignKey(User, on_delete=models.CASCADE)