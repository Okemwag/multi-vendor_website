from rest_framework import serializers
from .models import Vendor, ProductCategory, Product


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['user', 'email', 'address']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
