from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
# Create your views here.
@permission_required('is_staff', login_url=reverse_lazy('usuario:login'))
def index(request):
    return render(request, 'index.html')
