from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Mod

class OwnView(TemplateView):
    template_name = "main.html"

class RubricView(ListView):
    template_name = "list.html"
    model = Mod
    context_object_name = "list"
