from django.db import models

# Create your models here.
class method(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    branch=models.CharField(max_length=70)

    def __str__(self):
        return self.name

class employee(models.Model):
    emp_name=models.CharField(max_length=70)
    emp_salary=models.IntegerField()

    def __str__(self):
        return self.emp_name