from django.forms import ModelForm
from main.models import Product
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock", "image", "availability", "discount"]

    # Menggunakan pendekatan yang membuat lebih mudah untuk kustomisasi

    name = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
        required=True
    )
    price = forms.DecimalField(
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'})
    )
    stock = forms.IntegerField(
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock'})
    )
    image = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )
    availability = forms.ChoiceField(
        choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')],
        required=True,
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
    discount = forms.IntegerField(
        min_value=0,
        max_value=100,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Discount'})
    )


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )
