from django import forms

from produto.models import Produto

class ProdutoForm(forms.Form):
    class Meta:
        model = Produto
        fields = '__all__'