from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def cliente_home(self):

    if self.user.groups.filter(name='Gerentes').exists():
        print("gerente")
        return render(self, 'clientes/gerente.html')
    elif self.user.groups.filter(name='Clientes').exists():
        print("cliente")
        return render(self, 'clientes/cliente.html')