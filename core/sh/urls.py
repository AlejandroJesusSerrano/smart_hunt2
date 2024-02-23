from django.urls import path
from core.sh.views import *

urlpatterns = [
  path('uno/', my_first_view),
]