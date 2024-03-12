from django.urls import path
from core.sh.views.province.views import ProvinceCreateView, ProvinceDeleteView, ProvinceListView, ProvinceUpdateView

app_name = 'sh'

urlpatterns = [
  path('province/list/', ProvinceListView.as_view(), name='province_list'),
  path('province/add/', ProvinceCreateView.as_view(), name='province_add'),
  path('provice/edit/<int:pk>/', ProvinceUpdateView.as_view(), name='province_edit'),
  path('provice/delete/<int:pk>/', ProvinceDeleteView.as_view(), name='province_delete'),
]