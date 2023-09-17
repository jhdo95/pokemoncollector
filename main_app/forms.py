from django.forms import ModelForm
from .models import Berries, Item

class BerriesForm(ModelForm):
  class Meta:
    model = Berries
    fields = ['date', 'snack']
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']