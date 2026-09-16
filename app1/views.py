from django.http import HttpResponse

def inicio(request):
     return HttpResponse("<h1>Bienvenido a mi aplicación App1</h1>")
def informacion(request):
      return HttpResponse("<h1>Información de App1</h1><p>Esta es mi segunda vista.</p>")
