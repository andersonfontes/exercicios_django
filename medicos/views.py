from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Especialidade, Medico
from .forms import EspecialidadeForm, MedicoForm
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




class EspecialidadeListView(LoginRequiredMixin, ListView):
    model = Especialidade
    template_name = 'especialidade_list.html'
   

class EspecialidadeCreateView(LoginRequiredMixin, CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')


class EspecialidadeUpdateView(LoginRequiredMixin,UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_list')


class EspecialidadeDeleteView(LoginRequiredMixin, DeleteView):
    model = Especialidade
    template_name = 'especialidade_confirm_delete.html'
    success_url = reverse_lazy('especialidade_list')


class MedicoListView(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'medico_list.html'
    

class MedicoCreateView(LoginRequiredMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')


class MedicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_list')


class MedicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = 'medico_confirm_delete.html'
    success_url = reverse_lazy('medico_list')

def homepage(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())