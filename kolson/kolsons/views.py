from django.shortcuts import render
from kolsons.models import Product



def enquiry(request):
    return render(request, 'enquiry.html')
def about(request):
    return render(request, 'about.html')
def contactus(request):
    return render(request, 'contactus.html')
def market(request):
    return render(request, 'market.html')
def product(request):
    product = Product.objects.all()
    return render(request, 'product.html',{'product': product})
def client(request):
    return render(request, 'client.html')
def certifications(request):
    return render(request, 'certifications.html')
def productpost(request,id):
    product = Product.objects.filter(part_no=id).first()
    return render(request,'kolsons/productpost.html' , {'product': product})
