from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Especialidade, Medico
from .forms import EspecialidadeForm, MedicoForm

class EspecialidadeListView(ListView):
    model = Especialidade
    template_name = 'especialidade_list.html'

class EspecialidadeCreateView(CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')

class EspecialidadeUpdateView(UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')

class EspecialidadeDeleteView(DeleteView):
    model = Especialidade
    template_name = 'especialidade_confirm_delete.html'
    success_url = reverse_lazy('especialidade_list')

class MedicoListView(ListView):
    model = Medico
    template_name = 'medico_list.html'

class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medico_confirm_delete.html'
    success_url = reverse_lazy('medico_list')
