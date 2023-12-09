from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logouts
from django.contrib.auth.decorators import login_required
from home.models import Contact,Patient,Doctor

from django.core.mail import send_mail
# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    data1=Patient.objects.all()
    lst=[]
    ast=[]
    est=[]
    sst=[]
    pst=[]
    mst=[]
    for a in data1:
        lst.append(a.name)
    for a in data1:
        ast.append(a.age)
    for a in data1:
        sst.append(a.sex)
    for a in data1:
        pst.append(a.patId)
    for a in data1:
        mst.append(a.history)
    for a in data1:
        est.append(a.email)
    data={
          "Namedetails":lst,
          "AgeDetails":ast,
          "SexDetails":sst,
          "patIdDetails":pst,
          "medDetails":mst,
          "emailDetails":est
    }
    return render(request,"dashboard.html",data)
@login_required(login_url="login")
def medicine(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        patId=request.POST.get("patId")
        medicine=request.POST.get("medicine")
        message=request.POST.get("message")
        details="Patient with name "+name+" and Pat Id "+patId+"medicines are "+medicine
        
        send_mail(
            message,
            details,
            settings.EMAIL_HOST_USER,
            ["aritra.chakraborty203@gmail.com"]
        )
        return redirect("dashboard")
    else:
        return render(request,"medicine.html")
@login_required(login_url="login")
def farmDash(request):
    return render(request,"farmDash.html")
def index(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get('email')
        job=request.POST.get("job")
        message=request.POST.get("message")
        contact=Contact(name=name,email=email,designation=job,message=message)
        contact.save()
        messages.success(request,"You message added successfully")
        return redirect('index')

    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpass=request.POST.get("cnf_password")
        if(password!=confirmpass):
            messages.error(request, "Password not matched please re-enter passwords")
        else:
            user=User.objects.create_user(uname,email,password)
            user.save()
            return redirect("login")

    return render(request,"signup.html")
def patDetails(request):
     if request.method=="POST":
        uname=request.POST.get("uname")
        age=request.POST.get("age")
        email=request.POST.get("email")
        sex=request.POST.get("sex")
        patId=request.POST.get("patId")
        medHist=request.POST.get("MedHistory")
        Patient1=Patient(name=uname,age=age,email=email,sex=sex,patId=patId,history=medHist)
        Patient1.save()
        messages.success(request,"You message added successfully")

     return render(request,"pat.html")
def Login(request):
   
    if request.method=="POST":
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            return HttpResponse("Invalid username or password")

    return render(request,"login.html")
def loginPatient(request):
    return render(request,"patLogin.html")
def logout(request):
    logouts(request)
    return redirect("main")

def appointedDoctor(request):
    data1=Doctor.objects.all()
    nst=[]
    est=[]
    dst=[]
    sst=[]
 
    for a in data1:
        nst.append(a.doctor)
    for a in data1:
        est.append(a.email)
    for a in data1:
        dst.append(a.Degree)
    for a in data1:
       sst.append(a.Specialist)

    data={
          "NameDetails":nst,
          "emailDetails":est,
          "SpecialistDetails":sst,
          "DegreeDetails":dst,
    }
    return render(request,"appointDoctor.html",data)
def patLog(request):
    data1=Patient.objects.all()
    nst=[]
    pst=[]
    for a in data1:
        nst.append(a.name)
    for a in data1:
        pst.append(a.patId)
    if request.method=="POST":
        name=request.POST.get("uname")
        pId=request.POST.get("Pid")
        if (name in nst) and (pId in pst):
            return redirect("/apptDoc")
    return render(request,"patLogin.html")
def changeLog(request):
 data1=Patient.objects.all()
 nst=[]
 pst=[]
 for a in data1:
  nst.append(a.name)
 for a in data1:
    pst.append(a.patId)
 if request.method=="POST":
    name=request.POST.get("uname")
    pId=request.POST.get("Pid")
    if (name in nst) and (pId in pst):
        return redirect("/changeDoc")
 return render(request,"patLogin.html")
def changeDoc(request):
    data1=Doctor.objects.all()
    nst=[]
    est=[]
    dst=[]
    sst=[]
 
    for a in data1:
        nst.append(a.doctor)
    for a in data1:
        est.append(a.email)
    for a in data1:
        dst.append(a.Degree)
    for a in data1:
       sst.append(a.Specialist)

    data={
          "NameDetails":nst,
          "emailDetails":est,
          "SpecialistDetails":sst,
          "DegreeDetails":dst,
    }

    if request.method=="POST":
        value=request.POST.get("Doc")
        msg="The doctor details is name "+nst[int(value)]+" email "+est[int(value)]+"degree details "+dst[int(value)]+" specialization "+sst[int(value)]
        send_mail(
            "Please change the doctor",
            msg,
            settings.EMAIL_HOST_USER,
            ["aritra.chakraborty203@gmail.com"]
        )
        return redirect("index")
    else:
        return render(request,"changeDoc.html",data)