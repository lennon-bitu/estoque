from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
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
    
    