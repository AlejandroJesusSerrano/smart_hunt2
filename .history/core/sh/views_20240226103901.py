from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my_first_view(request):
  data = {
    'name': 'Alejandro'
  }
  return render(request, 'index.html', data)