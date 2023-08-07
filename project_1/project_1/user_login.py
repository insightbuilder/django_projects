from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from app_1.EmailBackEnd import EmailBackEnd

def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check email
        if User.objects.filter(email=email).exists():
           messages.warning(request,'Email are Already Exists !')
           return redirect('register')

        # check username
        if User.objects.filter(username=username).exists():
           messages.warning(request,'Username are Already exists !')
           return redirect('register')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request,'registration/register.html')

	
def DO_LOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
		
        user = EmailBackEnd.authenticate(request,
                                     username=email,
                                     password=password)
        if user!=None:
           login(request,user)
           return redirect('home')
        else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')

def PROFILE(request):
    return render(request, 'registration/profile_update.html')

def Profile_Update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        #The below conditions ensure that blank or none values are 
        #not updated in the database
        if username != None and username != "":
            user.username = username
        
        if email != None and email != '':
            user.email = email
        #Change in password will log the user out...
        if password != None and password != "":
            user.set_password(password)
        
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

def LOGOUT(request):
    logout(request)
    return redirect('home')
