from django.urls import path

from favorites import views

urlpatterns = [
    # path('', views.index, name='favorites_index'),
    path('add/<int:product_id>/<str:return_url>/', views.add_product, name='add_fav_product'),
    path('remove/<int:product_id>/<str:return_url>/', views.remove_product, name='remove_fav_product'),
]