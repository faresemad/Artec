from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.title