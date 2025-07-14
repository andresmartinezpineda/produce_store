from django import forms

class ProductSearchForm(forms.Form):
    """
    Search form to find products by name for adding to the sale.
    """
    search = forms.CharField(
        label='search Product',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'search product...'})
    )