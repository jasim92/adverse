from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def handleRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check erronous inputs
        if len(username) > 10:
            messages.error(request, "Username should be less than 10 chracters")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Username should be alphanumeric")
            return redirect('/')


        # creating user here
        myuser = User.objects.create_user(username, email, pass1) #creating user with the help of User(you have to import it. from django.contrib.auth.models import User)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save() # saving created user
        messages.success(request, "Your account has been created sucessfully")
        return redirect('/')
    else:
        return HttpResponse("404 not found")

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "You are sucessfully Loged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credential")
            return redirect('/')
    else: 
        return HttpResponse('handle login failed')
def handleLogout(request):
    logout(request)
    messages.success(request, "You are sucessfully Logged Out")
    return redirect('/')