from django.urls import path
from usuario import views as v

app_name = 'usuario'

urlpatterns = [
    path('',v.usuario_list, name='usuario_list'),
    path('<int:pk>/',v.usuario_detail, name='usuario_detail'),
    path('cadastrar',v.cadastro, name='cadastar_usuario'),
    path('login',v.loginSistema, name='login'),
    path('logout',v.logoutSistema, name='logout'),
    
]