from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Vacina
from .forms import VacinaForm

# Create your views here.
@login_required
def criar_vacina(request):
    # model = Vacina
    # form = VacinaForm(request.POST or None)

    # context = {
    #     'form': form
    # }

    # if str(request.method) == "POST":
    #     if form.is_valid():
    #         vacina = form.save()
    #         messages.success(request, 'Vacina cadastrada com sucesso')
    #         return redirect('listar_vacina')
    #     else:
    #         messages.error(
    #             request, 'Erro ao cadastrar vacina. Consulte o administrador.'                
    #         )
    # context['form'] = form

    return render(request, 'vacina/criar_vacina.html')
    