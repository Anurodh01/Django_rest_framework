from django.db import models

# Create your models here



class Employee(models.Model):
    name=models.CharField(max_length=20)
    email= models.EmailField(max_length=30)
    salary= models.IntegerField()
    phone= models.CharField(max_length=10)


    def __str__(self):
        return self.name