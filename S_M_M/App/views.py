from django.shortcuts import render,redirect
from .EmailBackEnd import EmailBackEnd
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
# Create your views here.

def Login(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate( request,
                                         username= request.POST.get('email'),
                                         password= request.POST.get('password') )
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('AdminHome')
            elif user_type == '2':
                return redirect('HodHome')
            elif user_type == '3':
                return redirect('StaffHome')
            else:
                return redirect('StudentHome')
        else:
            messages.error(request, ' Email or Password is invalid! ')
            return redirect('Login')
    else:
        messages.error(request, ' Email or Password is invalid! ')
        return redirect('Login')
    
def doLogout(request):
    logout(request)
    return redirect('Login')


def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        'user':user,
    }
    return render(request, 'profile.html', context)


def profileup(request):
    if request.method =="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, 'Profile is updated Successfully')
            return redirect('profile')
        except:
            messages.error(
                request, 'Your Profile Updation is Unsuccessful Try Again')

    return render(request, 'profile.html')


