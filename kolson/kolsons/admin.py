from django.contrib import admin
from .models import Product
from .clients import clientsM
# Register your models here.


admin.site.register(Product)

@admin.register(clientsM)
class clinetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo', 'companyName')
    

