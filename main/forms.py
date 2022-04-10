from django.forms import ModelForm, TextInput
from main.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['value']

        widgets = {
            'value' : TextInput(attrs={'id': 'new-item'}) 
        }

