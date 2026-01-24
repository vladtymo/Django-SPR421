from django.shortcuts import render

from favorites.favorites import get_favorite_products
from products.models import Product

def index(request, filter_by_favorites=False):
    products = Product.objects.all()

    filter_text = request.GET.get("filter_text", "")

    if filter_by_favorites:
        fav_ids = get_favorite_products(request)
        products = products.filter(id__in=fav_ids)

    if filter_text:
        products = products.filter(name__icontains=filter_text)

    return render(request, 'home/index.html', {
        'products': products, 
        "fav_ids": get_favorite_products(request),
    })
