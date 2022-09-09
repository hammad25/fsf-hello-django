from django import forms
from .models import Item

# using django built-in functionality forms.ModelForm
# the Meta class gives our form some information about 
# itself, such as which fields to render, or how to display errors

# Note: Remember, the fields: ‘name’ and ‘done’, have already been defined in models.py

class ItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ['name', 'done']
