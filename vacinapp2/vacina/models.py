from django.db import models

# Create your models here.
class Vacina(models.Model):
    vacina_nome = models.CharField('Vacina', max_length=250)
    vacina_lote = models.CharField('Lote', max_length=250)