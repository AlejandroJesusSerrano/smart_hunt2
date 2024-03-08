from django.urls import path
from core.sh.views.province.views import ProvinceCreateView, ProvinceListView, ProvinceUpdateView

app_name = 'sh'

urlpatterns = [
  path('province/list/', ProvinceListView.as_view(), name='province_list'),
  path('province/add/', ProvinceCreateView.as_view(), name='province_add'),
  path('provice/eidt/<int:pk>/', ProvinceUpdateView.as_view(), name='province_edit'),
]