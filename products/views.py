from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/detail.html', {'product': product})

def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('list_products')
    