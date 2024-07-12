from rest_framework import serializers
from .models import *

class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShippingInfo
        fields='__all__'