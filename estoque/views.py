from django.shortcuts import render
from django.views.generic import ListView

from .models import Estoque

# Create your views here.
class HomepageEstoque(ListView):
    template_name = 'HomepageEstoque.html'
    model = Estoque