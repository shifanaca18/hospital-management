from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('department',views.department,name='department'),
    path('doctor',views.doctor,name='doctor'),
    path('booking',views.booking,name='booking')
]