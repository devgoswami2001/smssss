# Generated by Django 4.2 on 2023-05-05 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_attendance_course_attendance_report_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance_report',
            name='course',
        ),
        migrations.RemoveField(
            model_name='attendance_report',
            name='dep',
        ),
    ]
