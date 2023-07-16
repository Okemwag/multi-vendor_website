from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.VendorList.as_view(), name='vendor_list'),
    # path('product/', views.ProductList.as_view(), name='product_list'),

]
