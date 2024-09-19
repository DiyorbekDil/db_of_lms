from django.contrib import admin
from courses_enrollments.models import CoursesModel, EnrollmentsModel, StagesModel
# Register your models here.
admin.site.register(CoursesModel)
admin.site.register(EnrollmentsModel)
admin.site.register(StagesModel)