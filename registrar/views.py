from django.shortcuts import render
#from .forms import formPaciente
from .models import Registrado
# Create your views here.


def inicio (request):
    form = formPaciente(request.POST or None )
    context = {
        "form":form
    }

    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("nombre_form")
        obj = Registrado.objects.create(nombres=abc)


    return render(request, "inicio.html", context)