from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

from produto.models import Categoria, Produto, Unidademedida

# Create your views here.
def home(request):
    template_name = 'home.html'
    lista = Produto.objects.all()
    context = {'lista': lista}
    return render(request,  template_name, context )


def add(request):
    if request.method == 'GET':
        template_name = 'add.html'
        categ = Categoria.objects.all()
        und = Unidademedida.objects.all()
        prod = Produto.objects.all()
        indice = len(prod) - 1
        
        untimoProdCad = prod[indice]
        
        context = {'produto':untimoProdCad, 'categoria': categ, 'unidade':und}
        #return HttpResponse(untimoProdCad.codigo)
        return render(request,  template_name, context )
    else: 
        cod = request.POST.get('codigo')
        codbarras = request.POST.get('codigobarras')
        nome = request.POST.get('nome')
        unidademedida =  int(request.POST.get('unidademedida'))
        preco = request.POST.get('preco')
        ncm = request.POST.get('ncm')
        saldo = request.POST.get('saldo')
        categoria =  int(request.POST.get('categoria'))
        
        ativo = request.POST.get('ativo')
        if ativo == 'on':
            ativo = True
        else:
            ativo = False
        
        prod = Produto.objects.filter(codigo=cod).first()
        
        if prod:
            return HttpResponse('Codigo Já cadastrado')
        produto = Produto.objects.create(codigo=cod, ean=codbarras, nome=nome,
                                         unidademedida_id=unidademedida, preco=preco,
                                         ncm=ncm, saldoestoque=saldo, categoria_id=categoria, 
                                         ativo=ativo)
        produto.save()
        
        return HttpResponse('produto cadastrado com sucesso')
   
    
def editar(request, pk):
    if request.method == 'GET':
        template_name = 'editar.html'
        categ = Categoria.objects.all()
        und = Unidademedida.objects.all()
        obj = Produto.objects.get(pk=pk)
        context = {'produto': obj,'categoria': categ, 'unidade':und}
        return render(request,  template_name, context )
    else:
        obj = Produto.objects.all()
        context = {'produto': obj}
        cod = request.POST.get('codigo')
        codbarras = request.POST.get('codigobarras')
        nome = request.POST.get('nome')
        unidademedida =  int(request.POST.get('unidademedida'))
        preco = request.POST.get('preco')
        preco = float(preco.replace(',', '.'))
        ncm = request.POST.get('ncm')
        saldo = request.POST.get('saldo')
        categoria =  int(request.POST.get('categoria'))
        
        ativo = request.POST.get('ativo')
        if ativo == 'on':
            ativo = True
        else:
            ativo = False
        prod = Produto.objects.filter(pk=pk).first()
        if prod:
            produto =  Produto.objects.filter(pk=pk).update(codigo=cod, ean=codbarras, nome=nome,
                                            unidademedida_id=unidademedida, preco=preco,
                                            ncm=ncm, saldoestoque=saldo, categoria_id=categoria, 
                                           ativo=ativo)
            #produto = Produto.objects.filter(pk=pk)
            #produto.save()
            
        return redirect('/produto/')
        
        
def datalhe_produto(request, pk):
    template_name = 'detalhe_produto.html'
    obj = Produto.objects.get(pk=pk)
    context = {'produto': obj}
    return render(request,  template_name, context )