from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('products', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),


    # path('', views.product_list, name='product_list'),
    # path('products/<int:pk>', views.product_detail, name='product_detail'),
    # path('products/new', views.product_create, name='product_create'),
    # path('products/<int:pk>/edit', views.product_edit, name='product_edit'),
    # path('products/<int:pk>/delete', views.product_delete, name="product_delete"),


]