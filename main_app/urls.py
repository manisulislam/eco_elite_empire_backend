from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('contact_us/', ContactUsList.as_view(),name='contact_us'),
    path('blogs/', BlogList.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    
]