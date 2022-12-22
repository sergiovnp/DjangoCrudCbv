from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Persona


class PersonaList(ListView):
    model = Persona

    def get_queryset(self):
        queryset = super(PersonaList, self).get_queryset()
        buscar = self.request.GET.get("buscar")
        if buscar:
            return queryset.filter(apellido__icontains=buscar)
        return queryset


class PersonaDetail(DetailView):
    model = Persona

