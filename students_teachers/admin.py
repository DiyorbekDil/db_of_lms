from django.contrib import admin
from students_teachers.models import StudentModel, TeachersModel, DepartmentsModel
# Register your models here.
admin.site.register(StudentModel)
admin.site.register(TeachersModel)
admin.site.register(DepartmentsModel)
