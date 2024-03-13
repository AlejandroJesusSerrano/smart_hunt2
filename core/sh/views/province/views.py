from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.sh.forms import ProvinceForm
from core.sh.models import Province

import logging

logger = logging.getLogger(__name__)

class ProvinceListView(ListView):
  model = Province
  template_name = 'provinces/list.html'

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    data = {}
    try:
      action = request.POST['action']
      if action == 'searchdata':
        data = []
        for p in Province.objects.all():
          data.append(p.toJSON())
      else:
        data['error'] = 'Se ha producido un error'
    except Exception as e:
      data['error'] = str(e)
    return JsonResponse(data, safe=False)


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
    context['prev'] = 'Listado de Provincias'
    context['title'] = 'Agregar Provincia'
    return context

class ProvinceDeleteView(DeleteView):
  model = Province
  template_name = 'provinces/delete.html'
  success_url = reverse_lazy('sh:province_list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Eliminar Provincia'
    context['entity'] = 'Provincias'
    context['list_url'] = reverse_lazy('sh:province_list')
    context['action'] = 'delete'
    context['prev'] = 'Listado de Provincias'
    context['title'] = 'Agregar Provincia'
    return context