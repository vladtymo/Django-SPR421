from django.shortcuts import get_object_or_404, redirect, render

from products.forms.product import ProductForm
from products.models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('list_products')
    product_form = ProductForm()
    return render(request, 'products/create.html', {'form': product_form})


def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('list_products')
    product_form = ProductForm(instance=product)
    return render(request, 'products/update.html', {'form': product_form})

def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('list_products')
    