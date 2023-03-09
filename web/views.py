from django.shortcuts import render
from django.http import HttpResponse
from web.forms import PistolaFormulario ,AsaltoFormulario,DmrFormulario
from web.models import pistolas,aSalto,dMr

def inicio(request):
    
    return render(request,'inicio.html')

def Pistolas(request):
    if request.method == 'POST':
        miformulario= PistolaFormulario(request.POST)
       
        print(miformulario)

        if miformulario.is_valid():
                
                informacion=miformulario.cleaned_data
                
                Pistola=pistolas(nombre=informacion['nombre'],fps=informacion['fps'])
                
                Pistola.save()
                
                return render(request,"inicio.html")
    else:
         miformulario= PistolaFormulario()
    return render(request, 'pistolas.html', {'miformulario': miformulario})

def asalto(request):
    if request.method == 'POST':
        miformulario=AsaltoFormulario(request.POST)
       
        print(miformulario)

        if miformulario.is_valid():
                
                informacion=miformulario.cleaned_data
                
                asalto=aSalto(nombre=informacion['nombre'],
                tipo=informacion['tipo'],
                fps=informacion['fps'])
                
                asalto.save()
                
                return render(request,"inicio.html")
    else:
         miformulario= AsaltoFormulario()
    return render(request, 'asalto.html', {'miformulario': miformulario})

def dmr(request):
    if request.method == 'POST':
        miformulario=DmrFormulario(request.POST)
       
        print(miformulario)

        if miformulario.is_valid():
                
                informacion=miformulario.cleaned_data
                
                dmr=dMr(nombre=informacion['nombre'],
                tipo=informacion['tipo'],
                fps=informacion['fps'])
                
                dmr.save()
                
                return render(request,"inicio.html")
    else:
         miformulario= DmrFormulario()
    return render(request, 'dmr.html', {'miformulario': miformulario})

def busquedapistola(request):
     
     return render(request,"busquedapistola.html")
def buscar(request):
    if 'fps' in request.GET:
        fPs = request.GET['fps']
        PIstolas = pistolas.objects.filter(fps__icontains=fPs)
        return render(request, "resultadosporbusqueda.html", {"pistolas": PIstolas, "fps": fPs})
    else:
        respuesta = "no enviaste datos"
        return render(request, "inicio.html", {"respuesta": respuesta})