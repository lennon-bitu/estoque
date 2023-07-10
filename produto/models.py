from django.db import models


# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Unidademedida(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=3)
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.codigo


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=40)
    ean = models.CharField(max_length=13, blank=True, null=True)
    preco = models.FloatField()
    unidademedida = models.ForeignKey(Unidademedida, on_delete=models.CASCADE)
    ncm = models.CharField(max_length=8)
    saldoestoque = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #cadastro = models.DateField()

    def __str__(self):
        return self.nome



