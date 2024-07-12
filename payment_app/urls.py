# urls.py

from django.urls import path
from .views import sslcommerz_init, sslcommerz_ipn

urlpatterns = [
    path('init/', sslcommerz_init, name='sslcommerz_init'),
    path('ipn/', sslcommerz_ipn, name='sslcommerz_ipn'),
]
