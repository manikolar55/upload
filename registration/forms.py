from django import forms
from .models import city_names

class edit_cityy(forms.ModelForm):
    class Meta:
        model=city_names
        fields="__all__"