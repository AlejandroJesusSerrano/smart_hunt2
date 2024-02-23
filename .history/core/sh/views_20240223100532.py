from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my_first_view(request):
  return HttpResponse('hola esta es mi primer url')