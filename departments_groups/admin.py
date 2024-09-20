from django.contrib import admin
from departments_groups.models import DepartmentsModel, GroupsModel, StagesModel
# Register your models here.
admin.site.register(DepartmentsModel)
admin.site.register(GroupsModel)
admin.site.register(StagesModel)