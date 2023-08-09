from hashlib import md5
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
@permission_required('is_staff', login_url=reverse_lazy('usuario:login'))
def usuario_list(request):
    template_name = 'usuario_list.html'
    user = User.objects.all()
    context = {'usuarios':user}
    return render(request, template_name, context)


def usuario_detail(request, pk):
    template_name = 'usuario_detail.html'
    user = User.objects.get(pk=pk)
    context = {'usuario':user}
    return render(request, template_name, context)


def cadastro(request):
    template_name = 'cadastro_user.html'
    if request.method == "GET":
            return render(request, template_name)
    else:
        username = request.POST.get('username')
        primeiro_nome = request.POST.get('primeironome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmasenha = request.POST.get('confirmasenha')
        
        user = User.objects.filter(username=username).first()
        
        if user or senha != confirmasenha:
          return render(request, template_name)
      
        user = User.objects.create_user(username, email, senha, first_name =  primeiro_nome, last_name = sobrenome )
        
        return HttpResponseRedirect('/usuario/')
    
    
def login(request):
    template_name = 'login.html'
    if request.method == 'GET':
        return render(request, template_name)
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=usuario).first()
        if user and user.username == usuario:
            return HttpResponse('usuario logado')
        else:
            return HttpResponse('usuario não encontrado')
    
      
    