from django.db import models

from vacina.models import Vacina
from paciente.models import Paciente
from unidade_saude.models import Unidade_Saude

# Create your models here.
class CadastroVacinal(models.Model):
    status_vacinacao = [
        ('Processamento', 'Processamento'),
        ('Completo', 'Completo'),
        ('Recusado', 'Recusado'),
    ]

    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    unidade_saude = models.ForeignKey(Unidade_Saude, on_delete=models.CASCADE)
    data_aplicacao = models.DateField('Data da aplicação')
    status = models.CharField('Status', choices=status_vacinacao)
