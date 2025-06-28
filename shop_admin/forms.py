from django import forms
from .models import Product,Category

class CategoryForm(forms.ModelForm):
    # Form for creating or updating product categories.
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter category name'}),
        }
        
class ProductForm(forms.ModelForm):

    #Form for creating or updating products in the inventory.
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'unit', 'category']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Stock quantity'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

