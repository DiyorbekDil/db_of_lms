from django.db import models

from courses_enrollments.models import CoursesModel
from students_teachers.models import Common, StudentModel


class AssignmentModel(Common):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    course = models.ForeignKey(CoursesModel, related_name='assignment',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'assignment'
        verbose_name_plural = 'assignments'


class SubmissionsModel(Common):
    submission_date = models.DateTimeField(auto_now_add=True)
    grade = models.PositiveSmallIntegerField()

    student = models.ForeignKey(StudentModel, related_name='submission',
                                on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentModel, related_name='submission',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'submission'
        verbose_name_plural = 'submissions'
