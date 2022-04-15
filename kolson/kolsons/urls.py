from django.urls import path
from .import views

urlpatterns = [
    path('enquiry',views.enquiry,name='enquiry'),
    path('about',views.about,name='about'),
    path('client',views.client,name='client'),
    path('certifications',views.certifications,name='certifications'),
    path('certificatedoc/<int:id>',views.certificateDoc,name='certificateDoc'),
    path('contactus',views.contactus,name='contactus'),
    path('market',views.market,name='market'),
    path('product',views.product,name='product'),
    path('enquiryform',views.enquiry_form,name='enquiryform'),
    path('product/<int:id>',views.productpost,name='productpost'),
] 