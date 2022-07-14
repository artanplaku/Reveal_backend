from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from rest_framework import generics
from .serializers import ProductSerializer
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'reveal_app/product_list.html', {'products': products})


# def product_detail(request, pk):
#     product = Product.objects.get(id=pk)
#     return render(request, 'reveal_app/product_detail.html', {'product': product})

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return redirect('product_detail', pk=product.pk)
#     else: 
#         form = ProductForm()
#     return render(request, 'reveal_app/product_form.html', {'form': form})


# def product_edit(request, pk):
#     product = Product.objects.get(pk=pk)
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance = product)
#         if form.is_valid():
#             product = form.save()
#             return redirect('product_detail', pk=product.pk)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'product/product_form.html', {'form': form})


# def product_delete(request, pk):
#     Product.objects.get(id=pk).delete()
#     return redirect('product_list')