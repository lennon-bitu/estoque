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
        ultimonum = int(prod[indice].codigo) + 1
        
        context = {'ultimonum':ultimonum, 'categoria': categ, 'unidade':und}
        #return HttpResponse(untimoProdCad.codigo)
        return render(request,  template_name, context )
    else: 
        cod = request.POST.get('codigo')
        codbarras = request.POST.get('codigobarras')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        ncm = request.POST.get('ncm')
        saldo = request.POST.get('saldo')
        estoquemin = request.POST.get('estoquemin')
        estoquemax = request.POST.get('estoquemax')
        #faz a busca do nome da unidade de medida e pega seu id para salvar na chave estrangeira no produto
        unidademedida =  request.POST.get('unidademedida')
        uni = Unidademedida.objects.get(nome=unidademedida)
        unidademedida = uni.pk
        
        categoria =  request.POST.get('categoria')
        cat = Categoria.objects.get(nome=categoria)
        categoria =  cat.pk
        
    
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
                                         ncm=ncm,estoquemin=estoquemin, estoquemax= estoquemax, saldoestoque=saldo, categoria_id=categoria, 
                                         ativo=ativo)
        produto.save()
        
        #return HttpResponse(cat.pk)
        return redirect('/produto/')
   
    
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
        cod = request.POST.get('codigo')
        codbarras = request.POST.get('codigobarras')
        nome = request.POST.get('nome')
        unidademedida =  int(request.POST.get('unidademedida'))
        preco = request.POST.get('preco')
        preco = float(preco.replace(',', '.'))
        ncm = request.POST.get('ncm')
        saldo = request.POST.get('saldo')
        estoquemin = request.POST.get('estoquemin')
        estoquemax = request.POST.get('estoquemax')
        categoria =  request.POST.get('categoria')
        cat = Categoria.objects.get(nome=categoria)
        categoria =  cat.pk
        
        ativo = request.POST.get('ativo')
        if ativo == 'on':
            ativo = True
        else:
            ativo = False
        prod = Produto.objects.filter(pk=pk).first()
        if prod:
            produto =  Produto.objects.filter(pk=pk).update(codigo=cod, ean=codbarras, nome=nome,
                                         unidademedida_id=unidademedida, preco=preco,
                                         ncm=ncm,estoquemin=estoquemin, estoquemax= estoquemax, saldoestoque=saldo, categoria_id=categoria, 
                                         ativo=ativo)
            #produto = Produto.objects.filter(pk=pk)
            #produto.save()
            
        return redirect('/produto/')
        
def deletar(request, pk):
    prod = Produto.objects.filter(pk=pk).first()
    if prod:
        produto =  Produto.objects.filter(pk=pk).delete()
    return redirect('/produto/')
     
            
def datalhe_produto(request, pk):
    template_name = 'detalhe_produto.html'
    obj = Produto.objects.get(pk=pk)
    context = {'produto': obj}
    return render(request,  template_name, context )