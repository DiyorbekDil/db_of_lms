from django.db import models
from students_teachers.models import Common, TeachersModel, StudentModel
from departments_groups.models import StagesModel


class CoursesModel(Common):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(TeachersModel, related_name='course',
                                on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(StagesModel, related_name='course',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class EnrollmentsModel(Common):
    enrollment_date = models.DateTimeField(auto_now_add=True)
    grade = models.PositiveSmallIntegerField(null=True, blank=True)

    student = models.ForeignKey(StudentModel, related_name='enrollment',
                                on_delete=models.CASCADE)
    course = models.ForeignKey(CoursesModel, related_name='enrollment',
                               on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} {self.course}"

    class Meta:
        verbose_name = 'enrollment'
        verbose_name_plural = 'enrollments'
