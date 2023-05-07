from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def StaffHome(request):
    return render(request, 'Staff/Home.html')


def TakeAttendence(request):
    staff = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff)
    subjectt = Subject.objects.get(staff=staff)
    dep = Department.objects.get(id=staff.dep.id)
    course = Course.objects.get(id=subjectt.course.id)
    context = {
        'subject': subject,
        'dep': dep,
        'course': course, }
    return render(request, 'Staff/TakeAttendence.html', context)


def ViewAttendence(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        depid = request.POST.get('depid')
        courseid = request.POST.get('courseid')
        getsub = Subject.objects.get(id=subject_id)
        getdep = Department.objects.get(id=depid)
        getcor = Course.objects.get(id=courseid)
        subject = Subject.objects.filter(id=subject_id)
        for s in subject:
            student_id = s.course.id
            students = Student.objects.filter(course_id=student_id)
    context = {
        'getsub': getsub,
        'getdep': getdep,
        'getcor': getcor,
        'students': students,
    }
    print(context)
    return render(request, 'Staff/ViewAttendance.html', context)


def SaveAttendence(request):
    if request.method == "POST":
        att_date = request.POST.get('att_date')
        subject_id = request.POST.get('subject_id')
        dep_id = request.POST.get('dep_id')
        course_id = request.POST.get('course_id')
        getsub = Subject.objects.get(id=subject_id)
        getdep = Department.objects.get(id=dep_id)
        getcor = Course.objects.get(id=course_id)
        attendance = Attendance(
            subject_id=getsub,
            att_date=att_date,
            course=getcor,
            dep=getdep,
        )
        attendance.save()
        is_present_list = request.POST.getlist('is_present')
        students_list = request.POST.getlist('student_id')

        for i in range(len(students_list)):
            student_id = students_list[i]
            is_present = True if is_present_list[i] == 'present' else False
            attendance_report = Attendance_report(
                student_id=Student.objects.get(id=student_id),
                is_present=is_present,
                att_id=attendance,
            )
            print(i)
            attendance_report.save()
        messages.success(request, 'Attendance saved successfully')
        return redirect('TakeAttendence')


def AttendenceReport(request):
    staff = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff)
    subjectt = Subject.objects.get(staff=staff)
    dep = Department.objects.get(id=staff.dep.id)
    course = Course.objects.get(id=subjectt.course.id)
    context = {
        'subject': subject,
        'dep': dep,
        'course': course, }
    return render(request, 'Staff/AttendenceReport.html', context)


def ViewAttendenceReport(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        att_datee = request.POST.get('att_date')
        depid = request.POST.get('depid')
        courseid = request.POST.get('courseid')
        getsub = Subject.objects.get(id=subject_id)
        getdep = Department.objects.get(id=depid)
        getcor = Course.objects.get(id=courseid)
        att = Attendance.objects.filter(subject_id=getsub, att_date=att_datee)
        att_report = []
        for a in att:
            attendance_id = a.id
            att_report += list(Attendance_report.objects.filter(att_id=attendance_id))
        context = {
            'getsub': getsub,
            'att_datee': att_datee,
            'getdep': getdep,
            'getcor': getcor,
            'att_report': att_report,
        }
        return render(request, 'Staff/ViewAttendenceReport.html', context)

def AllAttendence(request):
    staff = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff)
    subjectt = Subject.objects.get(staff=staff)
    dep = Department.objects.get(id=staff.dep.id)
    course = Course.objects.get(id=subjectt.course.id)
    context = {
        'subject': subject,
        'dep': dep,
        'course': course, }
    return render(request, 'Staff/AllAttendance.html', context)

def AllAttendenceReport(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        depid = request.POST.get('depid')
        courseid = request.POST.get('courseid')
        getsub = Subject.objects.get(id=subject_id)
        getdep = Department.objects.get(id=depid)
        getcor = Course.objects.get(id=courseid)
        att = Attendance.objects.filter(subject_id=getsub,dep=getdep,course=getcor).count()
        student = Student.objects.filter(course_id=getcor,dep=getdep)
        attendance_data_list = []
        for i in student:
            att_lec = Attendance_report.objects.filter(
                student_id = i.id,
                is_present=True,
                att_id__subject_id=getsub,
                att_id__dep=getdep,).count()
            total_lectures = att
            attended_lectures = att_lec
            if att > 0:
                attendance_percentage = round((att_lec / att) * 100, 2)
            else:
                attendance_percentage = 0.0
            attendance_data = {
                'roll_number': i.id,
                'name': f"{i.admin.first_name} {i.admin.last_name}",
                'total_lectures': total_lectures,
                'attended_lectures': attended_lectures,
                'attendance_percentage': attendance_percentage,
            }
            attendance_data_list.append(attendance_data)
        context = {
            'getsub': getsub,
            'getdep': getdep, 
            'getcor': getcor, 
            'attendance_data_list': attendance_data_list
            }
        return render(request, 'Staff/AllATTREPORT.html', context )


