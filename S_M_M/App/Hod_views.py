from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def HodHome(request):
    return render(request, 'Hod/Home.html')


def AddCourse(request):
    hod = Hod.objects.get(admin=request.user.id)

    if request.method == "POST":
        course_name = request.POST.get('course_name')
        depid = request.POST.get('depid')

        dep = Department.objects.get(id=depid)
        course = Course(
            name=course_name,
            dep=dep
        )
        course.save()
        messages.success(request, 'Course Added Successfully')
        return redirect('AddCourse')
    context = {
        'hod': hod,
    }
    return render(request, 'Hod/AddCourse.html', context)


def ViewCourse(request):
    hod = Hod.objects.get(admin=request.user.id)
    course = Course.objects.filter(dep=hod.dep)
    context = {
        'course': course,
    }
    return render(request, 'Hod/ViewCourse.html', context)


def EditCourse(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'Hod/EditCourse.html', context)


def UpdateCourse(request):
    if request.method == "POST":
        course_id = int(request.POST.get('course_id'))
        course_name = request.POST.get('course_name')
        course = Course.objects.get(id=course_id)
        course.name = course_name
        course.save()
        messages.success(request, 'Course updated successfull')
        return redirect('ViewCourse')


def DeleteCourse(request, id):
    try:
        course = Course.objects.get(id=id)
        course.delete()
        messages.success(request, 'Course Deleted Sucessfully')
        return redirect('ViewCourse')
    except:
        messages.error(
            request, 'Course cant be Deleted Student and Ataff is present ')
        return redirect('ViewCourse')


def AddStaff(request):
    hod = Hod.objects.get(admin=request.user.id)
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        depid = request.POST.get('depid')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Registered')
            return redirect('AddStaff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'UserName Is Already Registered')
            return redirect('AddStaff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()
            dep = Department.objects.get(id=depid)
            staff = Staff(
                admin=user,
                address=address,
                dep=dep,
                gender=gender,
            )
            staff.save()
            messages.success(
                request, f"The Staff name {user.first_name} {user.last_name} is successfully added")
            return redirect('AddStaff')
    context = {
        'hod': hod,
    }
    return render(request, 'Hod/AddStaff.html', context)


def ViewStaff(request):
    hod = Hod.objects.get(admin=request.user.id)
    staff = Staff.objects.filter(dep=hod.dep)
    context = {
        'staff': staff
    }
    return render(request, 'Hod/ViewStaff.html', context)


def EditStaff(request, id):
    staff = Staff.objects.filter(id=id)
    context = {
        'staff': staff
    }
    return render(request, 'Hod/EditStaff.html', context)


def UpdateStaff(request):
    if request.method == "POST":
        staff_id = int(request.POST.get('staff_id'))
        profile_pic = request.FILES.get('profile_pic')
        depid = request.POST.get('depid')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        password = request.POST.get('password')
        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address
        dep = Department.objects.get(id=depid)
        staff.dep = dep
        staff.save()
        messages.success(request, 'Information updated successfully')
        return redirect('ViewStaff')


def DeleteStaff(request, id):
    staff = CustomUser.objects.get(id=id)
    staff.delete()
    messages.success(request, ' Record deleted')
    return redirect('ViewStaff')


def AddStudent(request):
    hod = Hod.objects.get(admin=request.user.id)
    courses = Course.objects.filter(dep=hod.dep)
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        depid = request.POST.get('depid')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Registered')
            return redirect('AddStaff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'UserName Is Already Registered')
            return redirect('AddStaff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=4
            )
            user.set_password(password)
            user.save()
            dep = Department.objects.get(id=depid)
            course = Course.objects.get(id=course_id)
            student = Student(
                admin=user,
                address=address,
                dep=dep,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(
                request, f"The Student name {user.first_name} {user.last_name} is successfully added")
            return redirect('AddStudent')
    context = {
        'hod': hod,
        'courses': courses,
    }
    return render(request, 'Hod/AddStudent.html', context)


def ViewStudent(request):
    hod = Hod.objects.get(admin=request.user.id)
    student = Student.objects.filter(dep=hod.dep)
    context = {
        'student': student
    }
    return render(request, 'Hod/ViewStudent.html', context)


def EditStudent(request, id):
    hod = Hod.objects.get(admin=request.user.id)
    course = Course.objects.filter(dep=hod.dep)
    student = Student.objects.filter(id=id)
    context = {
        'student': student,
        'course': course,
    }
    return render(request, 'Hod/EditStudent.html', context)


def UpdateStudent(request):
    if request.method == "POST":
        Stu_id = int(request.POST.get('Stu_id'))
        profile_pic = request.POST.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        password = request.POST.get('password')
        address = request.POST.get('address')
        user = CustomUser.objects.get(id=Stu_id)
        user.first_name = first_name
        user.last_name = last_name
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)
        user.save()
        student = Student.objects.get(admin=Stu_id)
        student.gender = gender
        student.address = address
        course = Course.objects.get(id=course_id)
        student.course_id = course
        student.save()
        messages.success(request, 'Student Details Updated Successfully')
        return redirect('ViewStudent')


def DeleteStudent(request, id):
    student = CustomUser.objects.get(id=id)
    student.delete()
    messages.success(request, 'Student Deleted Sucessfully')
    return redirect('ViewStudent')


def AddSubject(request):
    hod = Hod.objects.get(admin=request.user.id)
    staff = Staff.objects.filter(dep=hod.dep)
    course = Course.objects.filter(dep=hod.dep)
    if request.method == "POST":
        sub_name = request.POST.get('sub_name')
        depid = request.POST.get('depid')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        dep = Department.objects.get(id=depid)
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(admin=staff_id)
        sub = Subject(
            name=sub_name,
            dep=dep,
            course=course,
            staff=staff,
        )
        sub.save()
        messages.success(request, 'Subject Added Sucessfully')
        return redirect('AddSubject')
    context = {
        'hod': hod,
        'staff': staff,
        'course': course,
    }
    return render(request, 'Hod/AddSubject.html', context)


def ViewSubject(request):
    hod = Hod.objects.get(admin=request.user.id)
    sub = Subject.objects.filter(dep=hod.dep)
    context = {
        'sub': sub
    }
    return render(request, 'Hod/ViewSubject.html', context)
