# Generated by Django 5.0.1 on 2024-01-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=70)),
                ('emp_salary', models.IntegerField()),
            ],
        ),
    ]