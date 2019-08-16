from django.shortcuts import render

# Create your views here.

def mivista(request):#marco la direccion para encontrar
    return render(request,'templates/apposolemio/index.html')