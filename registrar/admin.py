from django.contrib import admin
from .models import Registrado
from .forms import ReistradoForm
# Register your models here.



class AdminRegistrado(admin.ModelAdmin):

    list_display = ["__unicode__", "nombres", "actualizado"]
    form = ReistradoForm
    # class Meta:
    #     model = Registrado


admin.site.register(Registrado, AdminRegistrado)