from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('categories/', CategoryList.as_view(), name='categories'),
    
]