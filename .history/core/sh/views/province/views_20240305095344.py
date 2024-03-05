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
