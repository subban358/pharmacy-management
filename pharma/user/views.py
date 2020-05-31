from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import patientsPersonalDetail
from django.views.decorators.csrf import csrf_exempt
from .forms import patient_personalDetailForm
from django.core.mail import send_mail
from django.conf import settings

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
                subject = "Welcome to Pharmacy World"
                msg = "Greetings "+firstname+" we are glad to have you on board with us.\nYour health is our number one priority, explore your dashboard for all the world class services we provide.\n\nBest Regards,\nPharmacy World Team"
                from_email = settings.EMAIL_HOST_USER
                to_list = [email]
                send_mail(subject, msg, from_email, to_list, fail_silently=True)
                messages.info(request, "user created")
        else:
            messages.info(request, "passwords not matching")
            return redirect('signup')
    return redirect('/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')    

def dashboard(request):
    return render(request, 'dashboard.html')
@csrf_exempt
def patient_personalDetails(request): 
    current_user = request.user
    #userId = current_user.user_id
    userId = current_user.id
    sts = patientsPersonalDetail.objects.filter(user_id=userId)
    if len(sts.values_list()):
        d = {}
        details = sts.values_list()[0]
        print(details)
        d['status'] = True
        return render(request, 'patient_personalDetails.html',{'d': d})
    else:
        form = patient_personalDetailForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return home(request)
        return render(request, 'patient_personalDetails.html', {'form': form})
def edit(request):
    user = patientsPersonalDetail.objects.get(user_id=request.user.id)
    form = patient_personalDetailForm(request.POST, instance=user)
    if form.is_valid():
        update = patientsPersonalDetail()
        update.user = form.cleaned_data['user']
        update.dob = form.cleaned_data['dob']
        update.address = form.cleaned_data['address']
        update.mobile = form.cleaned_data['mobile']
        obj = form.save(commit=False)
        obj.save()
        return home(request)
    return render(request, 'edit.html', {'form': form})
