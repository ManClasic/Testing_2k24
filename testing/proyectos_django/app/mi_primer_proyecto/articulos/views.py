from django.shortcuts import render
from .forms import FormArticulo

def nuevo(request):
    context = {
        'form': FormArticulo()
    }
    return render(request, 'nuevo_articulo.html', context)