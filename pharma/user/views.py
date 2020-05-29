from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username = username, password = password)
    if user:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, "Invalid Credentials")
        return redirect('/')
    return home(request)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "username already taken")
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "email already taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, password = pass1, email = email, first_name = firstname, last_name = lastname)
                user.save()
                messages.info(request, "user created")
        else:
            messages.info(request, "passwords not matching")
            return redirect('signup')
    return redirect('/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')    