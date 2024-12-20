from django.shortcuts import render, redirect, reverse, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    # products = Product.objects.filter(user=request.user)
    last_login = request.COOKIES.get('last_login')

    context = {
        'website_title': 'Nai Express📦',
        'name': request.user.username,
        'class_name': 'PBP C',
        # 'products': products, 
        'last_login': last_login,

    }

    return render(request, "main.html", context)


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)  
            product.user = request.user  
            product.save() 
            return redirect('main:show_main') 
        else:
            return render(request, "create_product.html", {'form': form})
    else:
        form = ProductForm()

    return render(request, "create_product.html", {'form': form})

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = ProductForm(instance=product)

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id);
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = strip_tags(request.POST.get("name"))  
    description = strip_tags(request.POST.get("description"))  

    # Buat dan simpan produk baru tanpa membersihkan data saat testing
    new_product = Product(
        name=name, 
        description=description,
        price=request.POST.get("price"),
        stock=request.POST.get("stock"),
        availability=request.POST.get("availability"),
        image=request.FILES.get("image"),
        user=request.user
    )
    
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,  # Pastikan `user` diambil dari `request.user`
            name=data.get("name", ""),  # Pastikan ada nilai default jika kosong
            description=data.get("description", ""),
            price=data.get("price", "0.0"),
            stock=data.get("stock", 0),
            image=data.get("image", ""),  # Jika ada field image
            availability=data.get("availability", "In Stock"),
            discount=data.get("discount", "0.0"),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)