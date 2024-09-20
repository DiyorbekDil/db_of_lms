from django.db import models
from django.core.validators import MinLengthValidator
from departments_groups.models import DepartmentsModel, GroupsModel


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

    group = models.ForeignKey(GroupsModel, related_name='student',
                              on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class TeachersModel(Common):
    first_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=255, unique=True)

    department = models.ForeignKey(DepartmentsModel, related_name='teacher',
                                   on_delete=models.SET_NULL,
                                   null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
