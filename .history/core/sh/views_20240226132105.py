from django.http import HttpResponse
from django.shortcuts import render
from core.sh.models import Employee


# Create your views here.
def my_first_view(request):

  data = {
    'name': 'Alejandro',
    'employee': Employee.objects.all()
  }

  return render(request, 'index.html', data)