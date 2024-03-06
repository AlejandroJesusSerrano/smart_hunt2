from django.forms import ModelForm

from core.sh.models import Province

class ProvinceForm(ModelForm):
  class Meta:
    model = Province
    fields = '__all__'