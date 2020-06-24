from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import View
from .models import patientsPersonalDetail, Medicine, Order, DoctorDetail, Rating
from django.views.decorators.csrf import csrf_exempt
from .forms import patient_personalDetailForm, OrderForm, DoctorDetailForm, RatingForm
from django.core.mail import send_mail
from django.conf import settings
from .utils import render_to_pdf
from collections import defaultdict


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
@csrf_exempt
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
        #print(details)
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
    form = patient_personalDetailForm(request.POST or None, instance=user)
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

def buy_med(request):
    form = OrderForm(request.POST or None, initial={'patient' : request.user})
    if form.is_valid():
        qty = form.cleaned_data['quantity']
        med = form.cleaned_data['medicine']
        prv = Medicine.objects.filter(med_name=med).values()[0]['med_stock']
        pk = Medicine.objects.filter(med_name=med).values()[0]['id']
        price =  Medicine.objects.filter(med_name=med).values()[0]['med_price']
        update = Medicine.objects.get(id=pk)
        new = int(prv)-int(qty)
        if new <= 0:
            update.med_stock = 0
        else:
            update.med_stock = int(new)
        update.save()        
        #print(prv, qty)
        instance = form.save(commit = False)
        instance.patient = request.user
        instance.cost = int(price*qty)
        instance.save()
        oid = instance.id
        #print(oid)
        return bill(request, oid)
    return render(request, 'buy_med.html', {'form': form})    

def bill(request, oid):
    s = Order.objects.filter(id=oid).values()[0]
    order_id = s['id']
    ptn_id = s['patient_id']
    med_id = s['medicine_id']
    qty = s['quantity']
    date = s['date_of_order']
    cost = s['cost']
    u = User.objects.filter(id=ptn_id).values()[0]
    med = Medicine.objects.filter(id=med_id).values()[0]['med_name']
    price = Medicine.objects.filter(id=med_id).values()[0]['med_price']
    fname = u['first_name']
    lname = u['last_name']
    email = u['email']
    address = patientsPersonalDetail.objects.filter(user=request.user).values()[0]['address']
    contex = {
        'order_id':order_id,
        'ptn_id':ptn_id,
        'med':med,
        'qty':qty,
        'date':date,
        'cost':cost,
        'address':address,
        'price':price,
        'name':fname+" "+lname,
        'email':email
    }
    pdf = render_to_pdf('bill.html', contex)
    return HttpResponse(pdf, content_type='application/pdf')

def doctor(request):
    auth.logout(request)
    form = DoctorDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return doctorLogin(request)
    return render(request, 'doctor.html', {'form': form})
    
def doctorLogin(request):
    auth.logout(request)
    if request.method == 'POST':
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        query = DoctorDetail.objects.filter(DoctorEmail=email).values()[0]['DoctorPassword']
        if query==password:
            return render(request, 'doctorHome.html')
        else:
            messages.info(request, "Wrong Credentials")
            return render(request, 'wrong.html')   
    return render(request, 'doctorLogin.html')

def ratedoc(request):
    form = RatingForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save(commit=True)
        return home(request)
    return render(request, 'ratedoc.html', {'form': form})
def book(request):
    query = """
            SELECT D.id, D.DoctorName, D.Specialization, ROUND(AVG(R.rating), 1) AS 'Rating' FROM user_doctordetail D, user_rating R 
            WHERE D.id = R.doctor_id
            GROUP BY D.id
            ORDER BY Rating DESC LIMIT 5
            """
    got = Rating.objects.raw(query)        
    context = defaultdict()
    k = 1
    for i in got:
        context[i.DoctorName] = [k, i.Rating, i.Specialization]
        k += 1
    #print(context)        
    return render(request, 'book.html',{'context': context})    