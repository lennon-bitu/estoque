from django.urls import path
from produto import views as v

app_name = 'produto'

urlpatterns = [
    path('', v.home, name='home'),
    path('<int:pk>/', v.datalhe_produto, name='datalhe_produto'),
    path('add', v.add, name='incluir'),
    path('editar/<int:pk>/', v.editar, name='editar'),
    path('deletar/<int:pk>/', v.deletar, name='deletar'),
    
]