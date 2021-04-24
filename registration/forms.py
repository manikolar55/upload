from django import forms
from .models import city_names
from .models import server_products

class edit_cityy(forms.ModelForm):
    class Meta:
        model=city_names
        fields="__all__"


class HotelForm(forms.ModelForm):
    class Meta:
        model = server_products
        fields = ['name','img','desc','price']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = server_products
        fields = "__all__"
