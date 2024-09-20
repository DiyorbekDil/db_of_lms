from django.contrib import admin
from students_teachers.models import StudentModel, TeachersModel
# Register your models here.
admin.site.register(StudentModel)
admin.site.register(TeachersModel)
