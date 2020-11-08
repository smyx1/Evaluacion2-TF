from django.http import HttpResponse

def Saludar(request):
    return HttpResponse("Hola")