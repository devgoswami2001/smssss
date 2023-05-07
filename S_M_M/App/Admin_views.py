from django.shortcuts import render, redirect
from .models import Department
from django.contrib import messages
from .models import *

def AdminHome(request):
    return render(request, 'Admin/Home.html')

def Adddepartment(request):
    if request.method == "POST":
        dep_name = request.POST.get('dep_name')
        if Department.objects.filter(name=dep_name).exists():
            messages.warning(request, 'Department Already Exists')
        else:
            dep = Department(
                name=dep_name,
            )
            dep.save()
            messages.success(request, 'Department Added Successfully')
            return redirect('Adddepartment')
    return render(request, 'Admin/Adddep.html')

def Viewdepartment(request):
    dep = Department.objects.all()
    context = {
        'dep':dep
    }
    return render(request, 'Admin/Viewdep.html',context )

def Editdepartment(request,id):
    dep = Department.objects.get(id = id)
    context = {
        'dep':dep,
    }
    return render(request,'Admin/Editdep.html',context)

def Updatedepartment(request):
    if request.method == "POST":
        dep_name = request.POST.get('dep_name')
        dep_id = request.POST.get('dep_id')

        dep = Department.objects.get(id = dep_id )
        dep.name = dep_name
        dep.save()
        messages.success(request,'Department Updated Sucessfully')
        return redirect('Viewdepartment')

def Deletedepartment(request,id):
    try:
        dep = Department.objects.get(id=id)
        dep.delete()
        messages.success(request,'Department deleted successfully')
        return redirect('Viewdepartment')
    except:
        messages.error(request,'Department Cant Be deleted HOD is persent')
        return redirect('Viewdepartment')

def AddHod(request):
    depp = Department.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dep_id = request.POST.get('dep_id')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Registered')
            return redirect('AddHod')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'UserName Is Already Registered')
            return redirect('AddHod')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()
            dep = Department.objects.get(id=dep_id)
            hod = Hod(
                admin=user,
                address=address,
                dep = dep,
                gender=gender,
            )
            hod.save()
            messages.success(
                request, f"The Hod name {user.first_name} {user.last_name} is successfully added")
            return redirect('AddHod')
    context = {
        'depp':depp,
    }

    return render(request,'Admin/AddHod.html',context)

def ViewHod(request):
    hod = Hod.objects.all()
    context = {
        'hod':hod
    }
    return render(request, 'Admin/ViewHod.html',context)

def EditHod(request,id):
    depp = Department.objects.all()
    hod = Hod.objects.filter(id = id)
    context = {
        'hod':hod,
        'depp':depp,
    }
    return render(request,'Admin/EditHod.html',context)

def UpdateHod(request):
    if request.method == "POST":
        hod_id = int(request.POST.get('hod_id'))
        profile_pic = request.FILES.get('profile_pic')
        dep_id = request.POST.get('dep_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.get(id=hod_id)
        user.first_name = first_name
        user.last_name = last_name
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)
        user.save()

        hod = Hod.objects.get(admin=hod_id)
        hod.gender = gender
        hod.address = address
        dep = Department.objects.get(id=dep_id)
        hod.dep = dep
        hod.save()
        messages.success(request, 'Information updated successfully')
        return redirect('ViewHod')

def DeleteHod(request,id):
        hod = CustomUser.objects.get(id=id)
        hod.delete()
        messages.success(request,'Record deleted')
        return redirect('ViewHod')
