from django.shortcuts import render


def province_list (request):
  data = {
    'title': 'Listado de Provincias'
  }

  return render(request, 'provinces/list.html', data)
