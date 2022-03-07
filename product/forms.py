from django import forms
from django.forms import TextInput, Textarea, Select

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'active', 'price', 'category', 'is_stock', 'release', 'image']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter product name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter product description', 'class': 'form-control'}),
            'price': TextInput(attrs={'placeholder': 'Please enter product price', 'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'is_stock': Select(attrs={'class': 'form-control'}),
            'release': TextInput(attrs={'placeholder': 'Please enter the release date', 'class': 'form-control',
                                        'type': 'date'})
        }
