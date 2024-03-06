from typing import Any
from django.views.generic import ListView
from django.shortcuts import render
from core.sh.forms import ProvinceForm
from core.sh.models import Province

class ProvinceListView(ListView):
  model = Province
  template_name = 'provinces/list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Listado de Provincias'
    return context

class ProvinceCreateView(ListView):
  model = Province
  form_class = ProvinceForm
  template_name = 