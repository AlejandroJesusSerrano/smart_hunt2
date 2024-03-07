from django.http import HttpResponseRedirect
from django.shortcuts import render
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

  def post(self, request, *args, **kwargs):
      print(request.POST)
      form = ProvinceForm(request.POST)
      if form.is_valid():
        return HttpResponseRedirect(self.success_url)
      context = self.get_context_data(**kwargs)
      context['form'] = form
      return render(request, self.template_name, context)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Agregar Provincia'
    return context
