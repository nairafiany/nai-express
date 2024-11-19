from django.forms import ModelForm
from main.models import Product
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.html import strip_tags


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
        required=False,
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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        cleaned_name = strip_tags(name)
        if not cleaned_name:
            raise forms.ValidationError("Field name tidak boleh kosong setelah dibersihkan.")
        return cleaned_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        cleaned_description = strip_tags(description)
        if not cleaned_description:
            raise forms.ValidationError("Field description tidak boleh kosong setelah dibersihkan.")
        return cleaned_description
    


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
