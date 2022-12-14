from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    spec=models.CharField(max_length=50)
    dep=models.ForeignKey(Department, on_delete=models.CASCADE)
    image=models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_email=models.EmailField()
    p_phone=models.CharField(max_length=100)
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date=models.DateField() 
    booked_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.p_name