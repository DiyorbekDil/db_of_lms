# Generated by Django 5.1.1 on 2024-09-20 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_enrollments', '0002_alter_stagesmodel_options_and_more'),
        ('departments_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmodel',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='departments_groups.stagesmodel'),
        ),
        migrations.DeleteModel(
            name='StagesModel',
        ),
    ]
