from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil


# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(1,nSlides), 'product': products}
    return render(request, "shop/index.html")


def about(request):
    return render(request, "shop/about .html")


def contact(request):
    return HttpResponse("We Are At contact ")


def tracker(request):
    return HttpResponse("We Are At tracker ")


def search(request):
    return HttpResponse("We Are At search ")


def productview(request):
    return HttpResponse("We Are At productView ")


def checkout(request):
    return HttpResponse("We Are At checkout ")
