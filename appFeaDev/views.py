from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def esqueleto (request):
    return render(request, 'appFeaDev/templates/index.html')

def botLay1 (request):
    return render(request, 'appFeaDev/templates/botLay1.html')

def botLay2 (request):
    return render(request, 'appFeaDev/templates/botLay2.html')