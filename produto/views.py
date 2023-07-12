from django.shortcuts import render

from produto.models import Produto

# Create your views here.
def home(request):
    template_name = 'home.html'
    lista = Produto.objects.all()
    context = {'lista': lista}
    return render(request,  template_name, context )

def add(request):
    return render(request, 'add.html')