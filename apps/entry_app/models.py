
from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    salary = models.FloatField()
    address1 = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Classes(models.Model):
    name = models.CharField(max_length=200)
    floor_index = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    study_year = models.IntegerField()
    birthday = models.DateField()
    student_class = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    max_grade = models.FloatField(null=False, default=None)


class TeacherClassSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class StudentTcs(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tcs = models.ForeignKey(TeacherClassSubject, on_delete=models.CASCADE)
    take_exam = models.BooleanField(default=False)
    grade = models.FloatField()
