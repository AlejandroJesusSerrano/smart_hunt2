from typing import Any
from django.views.generic import ListView
from django.shortcuts import render
from core.sh.models import Province


def province_list (request):
  data = {
    'title': 'Listado de Provincias',
    'provinces': Province.objects.all(),
  }

  return render(request, 'provinces/list.html', data)

class ProvinceListView(ListView):
  model = Province
  template_name = 'provinces/list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Listado de Provincias'
    return super().get_context_data(**kwargs)