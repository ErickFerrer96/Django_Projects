from django.shortcuts import render, get_object_or_404

from personas.models import Persona


# Create your views here.
def detallePersona(request, id):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'personas/detalle.html', {'persona': persona})


