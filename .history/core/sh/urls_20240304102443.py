from django.urls import path
from core.sh.views.province import province_list

app_name = 'sh'

urlpatterns = [
  path('provinces/list/', province_list, name='province_list'),
]