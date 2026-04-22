from django.db import models

# Create your models here.


class StudentIDCard(models.Model):
    card_Id = models.FloatField()


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.ManyToManyField("Course", related_name="students")
    id_card = models.OneToOneField(StudentIDCard, on_delete=models.CASCADE)


class Coursedescription(models.Model):
    description = models.CharField(max_length=200)


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Semester(models.Model):
    semester = models.DateField(auto_now_add=True)


class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    description = models.OneToOneField(
        Coursedescription, on_delete=models.PROTECT)
    professor = models.ForeignKey(
        Professor, on_delete=models.SET_NULL, null=True)
