from django.shortcuts import render

def enquiry(request):
    return render(request, 'enquiry.html')
def about(request):
    return render(request, 'about.html')
def contactus(request):
    return render(request, 'contactus.html')
def market(request):
    return render(request, 'market.html')
def product(request):
    return render(request, 'product.html')
def client(request):
    return render(request, 'client.html')
def certifications(request):
    return render(request, 'certifications.html')
