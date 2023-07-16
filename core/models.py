from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Vendor model
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


# Product model
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)
    detail = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    images = models.ImageField(upload_to='images/', null=True, blank=True)
    productId = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
