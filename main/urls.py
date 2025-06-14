from django.urls import path
from .views import index, product_inner

urlpatterns = [
    path('', index, name='index'),
    path('product-inner/<int:pk>/', product_inner, name='product-inner'),
]
