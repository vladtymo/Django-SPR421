from django.urls import path

from products import views

urlpatterns = [
    path('', views.index),
    path('product/<int:id>/', views.product_detail),
]