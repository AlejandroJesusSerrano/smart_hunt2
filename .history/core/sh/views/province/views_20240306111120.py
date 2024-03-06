from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from core.sh.forms import ProvinceForm
from core.sh.models import Province

class ProvinceListView(ListView):
  model = Province
  template_name = 'provinces/list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Listado de Provincias'
    return context

class ProvinceCreateView(CreateView):
  model = Province
  form_class = ProvinceForm
  template_name = 'provinces/create.html'
  success_url = reverse_lazy('sh:province_list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Agregar Provincia'
    return context
