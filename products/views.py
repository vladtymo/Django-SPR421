from django.shortcuts import render

products = [
    {
        "id": 1,
        "name": "Wireless Mouse",
        "image_url": "https://picsum.photos/seed/wirelessmouse/800/400",
        "description": "Ergonomic wireless mouse with adjustable DPI.",
        "price": 29.99,
        "stock": 120,
        "category": "Electronics",
        "discount": 10,
    },
    {
        "id": 2,
        "name": "Notebook A5",
        "image_url": "https://picsum.photos/seed/notebooka5/800/400",
        "description": "A5 lined notebook with durable cover.",
        "price": 4.50,
        "stock": 500,
        "category": "Stationery",
        "discount": 0,
    },
    {
        "id": 3,
        "name": "Ceramic Coffee Mug",
        "image_url": "https://picsum.photos/seed/ceramicmug/800/400",
        "description": "350ml ceramic mug, dishwasher safe.",
        "price": 12.00,
        "stock": 200,
        "category": "Home",
        "discount": 5,
    }
]

def index(request):
    return render(request, 'products/index.html', {'products': products})

def product_detail(request, id):
    return render(request, 'products/detail.html', {'product': products[id - 1]})
