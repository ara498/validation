from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    semail=models.EmailField()
