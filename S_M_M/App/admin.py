from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class UserModel(UserAdmin):
    list_display = [ 'username', 'user_type' ]

admin.site.register(CustomUser,UserModel)
admin.site.register(Department)
admin.site.register(Hod)
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Attendance_report)