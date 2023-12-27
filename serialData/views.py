from django.shortcuts import render
import serial


# Create your views here.

ser = serial.Serial('COM10', 9600)
def index(request):
    arduino_data = ser.readline().decode().strip()
    
    return render(request,'index.html',{'arduino_data': arduino_data})

