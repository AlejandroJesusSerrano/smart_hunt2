from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.sh.forms import ProvinceForm
from core.sh.models import Province

class ProvinceListView(ListView):
  model = Province
  template_name = 'provinces/list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Listado de Provincias'
    context['create_url'] = reverse_lazy('sh:province_add')
    context['prev'] = 'Home'
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
        form.save()
        return HttpResponseRedirect(self.success_url)
      self.object = None
      context = self.get_context_data(**kwargs)
      context['form'] = form
      return render(request, self.template_name, context)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['prev'] = 'Listado de Provincias'
    context['title'] = 'Agregar Provincia'
    return context

class ProvinceUpdateView(UpdateView):
  model = Province
  form_class = ProvinceForm
  template_name = 'provinces/create.html'
  success_url = reverse_lazy('sh:province_list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Editar Provincia'
    context['entity'] = 'Provincias'
    context['list_url'] = reverse_lazy('sh:province_list')
    context['action'] = 'edit'
    return context