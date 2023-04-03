from django.db import models

class College(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='college_logos/')
    payment_code = models.CharField(max_length=20)
    # departments = models.ManyToManyField('CollegeDepartment', related_name='colleges')

    def __str__(self):
        return self.name

class CollegeDepartment(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='department_images/')
    colleges = models.ManyToManyField('College', related_name='departments')

    def __str__(self):
        return self.name