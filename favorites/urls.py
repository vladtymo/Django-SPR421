from django.urls import path

from favorites import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name='add_fav_product'),
    path('remove/<int:product_id>/', views.remove_product, name='remove_fav_product'),
]