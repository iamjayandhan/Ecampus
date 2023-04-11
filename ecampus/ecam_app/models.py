from django.db import models
from phone_field import PhoneField


# Create your models here.
class Student(models.Model):
    reg_no = models.CharField(primary_key=True)
    roll_no = models.CharField(max_length=10, unique=True)
    student_name = models.CharField(max_length=50)
    student_class = models.CharField(max_length=10)
    dob = models.DateField()
    mentor = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    phone_no = models.CharField()
    student_father_name = models.CharField(max_length=50)
    student_mother_name = models.CharField(max_length=50)
    Address = models.TextField(max_length=100)

    def __str__(self):
        return self.student_name
