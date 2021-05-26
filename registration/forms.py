from django import forms
from .models import city_names
from .models import server_products,orders

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
class orders_approve(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['username', 'product_names', 'product_descriptions', 'product_service', 'approved']