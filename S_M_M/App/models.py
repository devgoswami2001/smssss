from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1,'Admin'),
        (2,'HOD'),
        (3,'STAFF'),
        (4,'STUDENT'),
    )
    user_type = models.CharField(choices=USER, max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Department(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hod(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    dep = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    dep = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    dep = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"

class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    dep = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"
    
class Subject(models.Model):
    name = models.CharField(max_length=500)
    dep = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(Staff,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    att_date = models.DateField()
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING,default=3)
    dep = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.name

class Attendance_report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    att_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name