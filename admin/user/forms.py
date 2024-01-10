from django import forms
from.models import employee

class employeeform(forms.Form):
    emp_name=forms.CharField()
    emp_salary=forms.IntegerField()