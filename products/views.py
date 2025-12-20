from django.shortcuts import render

from products.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/detail.html', {'product': product})