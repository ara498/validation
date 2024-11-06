from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def student(request):
    SFO=StudentForms()
    d={'SFO':SFO}

    if request.method=='POST':
        SFO=StudentForms(request.POST)
        if SFO.is_valid():
            sid=request.POST['student_id']
            sname=request.POST['student_name']
            semail=request.POST['student_email']
            SDO=StudentDetails.objects.get_or_create(sid=sid,sname=sname,semail=semail)
            return HttpResponse(str(SFO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render (request,'student.html',d)            
