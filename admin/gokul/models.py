from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=70)
    emp_salary=models.IntegerField()


    def __str__(self):
        return self.emp_name
    

class articles(models.Model):
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120)
