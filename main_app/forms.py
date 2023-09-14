from django.forms import ModelForm
from .models import Berries

class BerriesForm(ModelForm):
  class Meta:
    model = Berries
    fields = ['date', 'snack']