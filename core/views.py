from django.shortcuts import render
from rest_framework import generics
from .models import Vendor, ProductCategory, Product
from core.serializers import VendorSerializer, ProductSerializer, ProductCategorySerializer


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
