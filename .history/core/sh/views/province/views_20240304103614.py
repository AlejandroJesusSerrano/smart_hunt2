from django.shortcuts import render


def province_list (request):
  data = {

  }

  return render(request, 'provinces/list.html', data)
