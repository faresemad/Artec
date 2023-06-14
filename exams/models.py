from django.db import models
from colleges.models import College


class MCQExam(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100, null=True, blank=True)
    option3 = models.CharField(max_length=100, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class DigitalDrawingExam(models.Model):
    question = models.CharField(max_length=255)
    task_description = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class HandDrawingExam(models.Model):
    question = models.CharField(max_length=255)
    task_description = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class PracticeDrawingExam(models.Model):
    question = models.CharField(max_length=255)
    task_description = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
