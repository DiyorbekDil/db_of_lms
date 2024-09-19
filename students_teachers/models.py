from django.db import models
from django.core.validators import MinLengthValidator


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StudentModel(Common):
    first_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=255, unique=True)
    enrollment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class TeachersModel(Common):
    first_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=255, unique=True)
    department = models.CharField(max_length=128, validators=[MinLengthValidator(8)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
