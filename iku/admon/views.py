from django.shortcuts import render
from .models import Cliente
def casita (request):
    listaCliente=Cliente.objects.all()
    
    return render(request,"inicio.html", {"cliente":listaCliente})
    
# Create your views here.
