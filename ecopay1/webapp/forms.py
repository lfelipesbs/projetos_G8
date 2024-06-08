from django import forms
from .models import Dados,Ocorrencia

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'senha', 'tipo']

class LoginForm(forms.Form):
    nome = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)
    tipo = forms.CharField(widget=forms.HiddenInput(), required=False)

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['descricao', 'endereco', 'tipo_de_lixo', 'data']

