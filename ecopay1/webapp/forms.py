from django import forms
from .models import Dados,Ocorrencia,Dica,Alerta,Avaliacao

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


class AlertaForm(forms.ModelForm):
    class Meta:
        model = Alerta
        fields = ['mensagem', 'local', 'tipo', 'acao']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'local': forms.TextInput(attrs={'maxlength': 255}),
            'tipo': forms.TextInput(attrs={'maxlength': 255}),
            'acao': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['avaliacao', 'observacoes']
        widgets = {
            'avaliacao': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'observacoes': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }
        labels = {
            'avaliacao': 'Avaliação (1-5)',
            'observacoes': 'Observações'
        }