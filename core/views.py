from django.shortcuts import render
from core.models import Cadastro

# Create your views here.

def index(request):
    cadastro = Cadastro.objects.all()
    context = {'cadastro': cadastro}
    return render(request, 'index.html', context)
