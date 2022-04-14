from django.shortcuts import render
from kolsons.models import Product

def index(request):
    product = Product.objects.all()
    return render(request, 'index.html',{'product':product})

def products(request):
    return render(request,'kolsons/enquiry.html')