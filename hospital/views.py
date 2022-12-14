from django.http import HttpResponse
from django.shortcuts import render
from . models import Department, Doctor, Booking
from . forms import BookingForm
def index(request):
    return render(request,'index.html')

def department(request):
    department=Department.objects.all()
    return render(request,'department.html',{'departments':department})

def doctor(request):
    doctor=Doctor.objects.all()
    return render(request,'doctor.html',{'doctors':doctor})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>')
    form = BookingForm()
    return render(request,'booking.html',{'form':form})