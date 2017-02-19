from django import forms
from .models import Registrado

# class formPaciente(forms.Form):
#
#     cedula_de_identidad = forms.IntegerField()
#     nombre_form = forms.CharField(max_length=100)
#     apellidos = forms.CharField(max_length=100)
#     fecha_nac = forms.DateField()
#     telefono = forms.IntegerField()
#     #actualizado = forms.DateTimeField()


class ReistradoForm(forms.ModelForm):
    class Meta:
        model= Registrado
        fields = ["nombres", "apellidos"]