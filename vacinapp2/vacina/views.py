from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def criar_vacina(request):
    form = VacinaForm()
    return render(request, 'vacina/criar_vacina.html', {'form':form})