from django.db import models


# Create your model
class StudentRecord(models.Model):
    CHOICES = (('first', 'First'),
               ('second', 'Second')
               )
    name = models.CharField(max_length=100, blank=False, null=False, default='Enter Name here')
    age = models.IntegerField(blank=True, null=False)
    year = models.CharField(choices=CHOICES, max_length=255, null=False, blank=False)
    register_date = models.DateTimeField(auto_now_add=True)

class StudentAddress(models.Model):
    city = models.CharField(max_length=255,blank=False,null=False)
    pin = models.IntegerField(blank=False,null=False)

class ClassRecord(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    register_date = models.DateTimeField(auto_now_add=True)
    studentname = models.ForeignKey(StudentRecord,on_delete=models.CASCADE ,blank=True,null=True)

class CollegeRecord(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='None')
    register_date = models.DateTimeField(auto_now_add=True)
    classname= models.ForeignKey(ClassRecord,on_delete=models.CASCADE ,blank=True,null=True)