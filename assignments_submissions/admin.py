from django.contrib import admin
from assignments_submissions.models import AssignmentModel, SubmissionsModel
# Register your models here.
admin.site.register(AssignmentModel)
admin.site.register(SubmissionsModel)