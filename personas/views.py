from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Persona


class PersonaList(ListView):
    model = Persona


class PersonaDetail(DetailView):
    model = Persona

