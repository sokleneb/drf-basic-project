from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name