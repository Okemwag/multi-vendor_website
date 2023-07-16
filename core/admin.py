from django.contrib import admin
from .models import *


for model in [Vendor, ProductCategory, Product]:
    admin.site.register(model)
