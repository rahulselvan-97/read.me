from django import forms
from.models import Employee

class employee_date(forms.Form):
    emp_name=forms.CharField()
    emp_salary=forms.IntegerField()


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)