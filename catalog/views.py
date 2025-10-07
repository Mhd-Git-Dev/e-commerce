from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.filter(active=True).order_by('-updated_at')
    return render(request, "catalog/index.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, active=True)
    return render(request, "catalog/product_detail.html", {"product": product})

# Create your views here.
