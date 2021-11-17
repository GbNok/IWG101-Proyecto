from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Problem(models.Model):
    statement = models.CharField(max_length=200)
    def __str__(self):
        return self.statement

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

