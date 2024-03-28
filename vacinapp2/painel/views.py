from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def painel_home(self):

    if self.user.groups.filter(name='Gerentes').exists():
        print("gerente")
        return render(self, 'painel/gerente.html')
    elif self.user.groups.filter(name='Clientes').exists():
        print("cliente")
        return render(self, 'painel/cliente.html')
    elif self.user.groups.filter(name='Unidades_Saude').exists():
        print("unidade_saude")
        return render(self, 'painel/unidade.html')
    elif self.user.groups.filter(name='Maternidade').exists():
        print("maternidade")
        return render(self, 'painel/maternidade.html')