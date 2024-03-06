from django.forms import ModelForm, TextInput

from core.sh.models import Province

class ProvinceForm(ModelForm):
  class Meta:
    model = Province
    fields = '__all__'
    labels = {
      'number_id': 'N° de Provincia'
    }
    widgets = {
      'number_id': TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Ingrese el numero identificatorio de la provincia',
          'autocomplete': 'off'
        }
      )
    }