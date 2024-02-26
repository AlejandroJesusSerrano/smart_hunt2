from django.urls import path
from core.sh.views import *

app_name = 'sh'

urlpatterns = [
  path('uno/', my_first_view, name='vista1'),
  path('dos/', my_second_view, name='vista2'),
]