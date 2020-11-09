from django.http import HttpResponse
from django.shortcuts import render

def Saludar(request):
    return HttpResponse("Hola")

def Index(request):
    return render(request, 'Index.html')