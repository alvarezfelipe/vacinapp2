from django import forms
from .models import *

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = [
            "vacina_nome",
            "vacina_lote"
        ]