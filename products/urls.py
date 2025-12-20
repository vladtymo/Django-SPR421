from django.urls import path

from products import views

urlpatterns = [
    path('list/', views.list_products, name='list_products'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
]