from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from nouapp.models import Student,Login,Enquiry
from studentapp.models import Sturesponse
from datetime import date
from.models import Materials,News
from django.contrib import messages

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,'adminhome.html',locals())
    except KeyError:
        return redirect('nouapp:login')


def adminlogout(request):
    try:
        del request.session['adminid']
    except KeyError:
        return redirect('nouapp:login')
    return redirect('nouapp:login')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudent(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            stu=Student.objects.all()
            return render(request,'viewstudent.html',locals())
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiry(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            enq=Enquiry.objects.all()
            return render(request,'viewenquiry.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewfeedback(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            feed=Sturesponse.objects.filter(responsetype='feedback')
            return render(request,'viewfeedback.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcomplain(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            comp=Sturesponse.objects.filter(responsetype='complain')
            return render(request,'viewcomplain.html',locals())
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def uploadmaterial(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=='POST':
                program=request.POST['program']
                branch=request.POST['branch']
                year=request.POST['year']
                subject=request.POST['subject']
                materialtype=request.POST['materialtype']
                filename=request.POST['filename']
                myfile=request.FILES['myfile']
                posteddate=date.today()
                mat=Materials(program=program,branch=branch,year=year,subject=subject,materialtype=materialtype,filename=filename,myfile=myfile,posteddate=posteddate)
                mat.save()
                messages.success(request,'material is uploaded')

            return render(request,'uploadmaterial.html',locals())
    except KeyError:
        return redirect('nouapp:login')
