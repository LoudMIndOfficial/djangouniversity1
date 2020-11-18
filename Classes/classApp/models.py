from django.db import models

# Create your models here.
class classApp(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.FloatField()

    objects = models.Manager()

    # def __str__(self):
    #     return self.name

