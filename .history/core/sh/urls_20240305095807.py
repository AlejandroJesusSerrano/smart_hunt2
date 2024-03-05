from django.urls import path
from core.sh.views.province.views import ProvinceListView

app_name = 'sh'

urlpatterns = [
  path('province/list/', ProvinceListView.as_view(), name='province_list'),
]