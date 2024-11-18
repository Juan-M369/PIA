from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def Agentes(request):
    return render(request,"Agentes.html")
def Mapas(request):
    return render(request,"Mapas.html")
def Arsenal(request):
    return render(request,"Arsenal.html")
def Equiposcom(request):
    return render(request,"Equiposcom.html")
