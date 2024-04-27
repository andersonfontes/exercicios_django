from django import forms
from .models import Especialidade, Medico

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome', 'descricao']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm', 'especialidade']