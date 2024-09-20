from django.db import models
from django.core.validators import MinLengthValidator
from courses_enrollments.models import StagesModel
# Create your models here.


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DepartmentsModel(Common):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(8)])
    established_at = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class GroupsModel(Common):
    name = models.CharField(max_length=128, validators=[MinLengthValidator(2)])

    stage = models.ForeignKey(StagesModel, related_name='group',
                              on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
