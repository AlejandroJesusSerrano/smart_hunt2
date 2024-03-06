from django.urls import path
from core.sh.views.province.views import ProvinceCreateView, ProvinceListView

app_name = 'sh'

urlpatterns = [
  path('province/list/', ProvinceListView.as_view(), name='province_list'),
  path('province/add/', ProvinceCreateView.as_view(), name='province_add'),
]