from django.db import models
from django.shortcuts import render
from EcomApp.models import Setting
from Product.models import Product

# Create your views here.


def Home(request):
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:2]
    latest_products = Product.objects.all().order_by('-id')
    products = Product.objects.all()

    context = {
        'setting': setting,
        'sliding_images': sliding_images,
        'latest_products': latest_products,
        'products': products,
    }
    return render(request, 'home.html', context)


def product_single(request, id):
    context = {}

    return render(request, 'product-single.html', context)
