from django import forms
from django.forms import ModelForm
from .models import Produto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit ,Layout,Div
from django.urls import reverse

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs.update({
            'step': '0.01'
        })
        self.fields['preco'].label = 'Preço'
        self.fields['imagem'].required = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('cadastro_produtos')
        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn btn-primary text-center'))
       
