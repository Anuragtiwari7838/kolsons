from django.shortcuts import render
import smtplib
from .clients import clientsM
from email.message import EmailMessage

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

# following function extract information of clints from database
def client(request):
    clients = clientsM.objects.all()
    return render(request, 'client.html',{'clients':clients})


def certifications(request):
    return render(request, 'certifications.html')

# enquiry form mailing function
def enquiry_form(request):
    name = request.POST['name']
    organisation = request.POST['organisation']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    pii = request.POST['pii']
    quantity = request.POST['quantity']
    comments = request.POST['comments']
     
        

    EMAIL_ADDRESS = 'nerthinksjareen@gmail.com'
    EMAIL_PASSWORD = 'Ironman@12'

    msg = EmailMessage()
    msg['Subject'] = 'contacting from enquiry form'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] =email
    mg = f"name:{name}\nOrganisation:{organisation}\nAdress:{address}\nPhone:{phone}\nEmail:{email}Product intrested in:{pii}\nQuantity:{quantity}\nComments/Suggestions/feedback:{comments}\n"

    msg.set_content(mg)
    
   
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

   
    return render(request,'enquiry.html')


