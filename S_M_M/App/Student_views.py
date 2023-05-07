from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def StudentHome(request):
    student = Student.objects.get(admin=request.user.id)
    depp = Department.objects.get(id=student.dep.id)
    course = Course.objects.get(id=student.course_id.id)
    subjects = Subject.objects.filter(course=course)
    attendance_data_list = []
    for i in subjects:
        att = Attendance.objects.filter(subject_id=i.id, dep=depp, course=course).count()
        att_lec = Attendance_report.objects.filter(
                student_id = student,
                is_present=True,
                att_id__subject_id=i.id,
                att_id__dep=depp,
            att_id__course=course).count()
        total_lectures = att
        attended_lectures = att_lec
        if att > 0:
            attendance_percentage = round((att_lec / att) * 100, 2)
        else:
            attendance_percentage = 0.0
        attendance_data = {
            'subject_name': i.name,
            'total_lectures': total_lectures,
            'attended_lectures': attended_lectures,
            'attendance_percentage': attendance_percentage,
        }
        attendance_data_list.append(attendance_data)

    return render(request, 'Student/Home.html', {'attendance_data_list': attendance_data_list})

def StudentViewAttendence(request):
    student = Student.objects.get(admin=request.user.id)
    dep = Department.objects.get(id=student.dep.id)
    course =Course.objects.get(id=student.course_id.id)
    subject = Subject.objects.filter(course=student.course_id)
    context = {
        'dep':dep,
        'course':course,
        'subject':subject,
    }
    return render(request,'Student/ViewAttendance.html',context)

def StudentDetailedAttendence(request):
    student = Student.objects.get(admin=request.user.id)
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        depid = request.POST.get('depid')
        courseid = request.POST.get('courseid')
        getsub = Subject.objects.get(id=subject_id)
        getdep = Department.objects.get(id=depid)
        getcor = Course.objects.get(id=courseid)
        att = Attendance.objects.filter(subject_id=getsub, dep=getdep, course=getcor).order_by('att_date')
        att_report = []
        for a in att:
            attendance_id = a.id
            att_report += list(Attendance_report.objects.filter(student_id=student.id,  att_id=attendance_id))
        context = {
            'getsub': getsub,
            'getdep': getdep,
            'getcor': getcor,
            'att_report': att_report,
        }
        return render(request, 'Student/allattendance.html', context)

