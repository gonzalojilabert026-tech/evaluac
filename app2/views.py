from django.shortcuts import render


def inicio(request):
    return render(request, 'app2/inicio.html')


def informacion(request):
    return render(request, 'app2/informacion.html')