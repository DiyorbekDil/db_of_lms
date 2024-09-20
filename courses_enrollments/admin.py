from django.contrib import admin
from courses_enrollments.models import CoursesModel, EnrollmentsModel
# Register your models here.
admin.site.register(CoursesModel)
admin.site.register(EnrollmentsModel)
