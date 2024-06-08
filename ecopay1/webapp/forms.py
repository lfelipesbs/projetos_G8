from django import forms
from .models import Dados,Ocorrencia,Dica

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

class DicaForm(forms.ModelForm):
    class Meta:
        model = Dica
        fields = ['tipo', 'texto']

