from django.shortcuts import redirect, render
from favorites.favorites import add_product_to_favorites, remove_product_from_favorites

def add_product(request, product_id):
    return_url = request.GET.get('next', '/')
    add_product_to_favorites(request, product_id)
    return redirect(return_url)

def remove_product(request, product_id):
    return_url = request.GET.get('next', '/')
    remove_product_from_favorites(request, product_id)
    return redirect(return_url)