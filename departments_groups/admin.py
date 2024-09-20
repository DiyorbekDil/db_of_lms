from django.contrib import admin
from departments_groups.models import DepartmentsModel, GroupsModel
# Register your models here.
admin.site.register(DepartmentsModel)
admin.site.register(GroupsModel)