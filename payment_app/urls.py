# urls.py

from django.urls import path
from .views import sslcommerz_init, sslcommerz_ipn,ShippingInfoList

urlpatterns = [
    path('init/', sslcommerz_init, name='sslcommerz_init'),
    path('ipn/', sslcommerz_ipn, name='sslcommerz_ipn'),
    path('shipping/',ShippingInfoList.as_view(),name='shipping')

    
]
