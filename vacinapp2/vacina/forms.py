from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit, Button

from django import forms
from .models import Vacina

class VacinaForm(forms.ModelForm):
    # class Meta:
    #     model = Vacina
    #     fields = [
    #         'vacina_nome',
    #         'vacina_lote',
    #     ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'POST'
    #     self.helper.form_action = '.'
    #     self.helper.add_input(
    #         Submit(
    #             "submit",
    #             "Salvar",
    #             css_class= "btn btn-dark"
    #         )
    #     )

    #     self.helper.add_input(
    #         Button(
    #             "voltar",
    #             "Voltar",
    #             css_class = "btn btn-outline-dark",
    #             onclick = "javascript:history.back()",
    #         )
    #     )

    #     self.helper.layout = Layout(
    #         Fieldset(
    #             "",
    #             Div(
    #                 Field("vacina_nome", wrapper_class="col"),
    #                 Field("vacina_lote", wrapper_class="col"),
                    
    #                 css_class = "row",
    #             ),
                
    #             css_class = "border-bottom mb-3"
    #         )
    #     )
    vacina_nome = forms.CharField(
        label = 'Nome da vacina:',
        max_length= 250,
        required= True,
    )

    vacina_lote = forms.CharField(
        label = 'Lote:',
        max_length= 250,
        required= True
    )

    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-form'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = '.'

    #     self.helper.add_input(Submit('submit', 'Submit'))