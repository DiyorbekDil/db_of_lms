# Generated by Django 5.1.1 on 2024-09-19 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students_teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoursesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='students_teachers.teachersmodel')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses_enrollments.stagesmodel')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='EnrollmentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.PositiveSmallIntegerField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='courses_enrollments.coursesmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='students_teachers.studentmodel')),
            ],
            options={
                'verbose_name': 'enrollment',
                'verbose_name_plural': 'enrollments',
            },
        ),
    ]
