from distutils.command.upload import upload
from django.db import models

# Create your models here. path("index/<int:id>",viewss.ind) , href="index/object.id"

class Product(models.Model):
    part_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=2000)
    images = models.ImageField(upload_to='document')
    pdf = models.FileField(upload_to='document')

    def __str__(self):
        return self.name

# creating model for clients database
class clientsM(models.Model):
    # id = models.IntegerField(primary_key=True)
    logo = models.ImageField(upload_to='clients/logos')
    companyName = models.CharField(max_length=200)

# creates model for certificats in database
class certificatsM(models.Model):
    certificateimage = models.ImageField(upload_to='certificats/image')
    certificatePDF = models.FileField(upload_to='certificats/pdf')
    certificateInfo = models.CharField(max_length=300)
