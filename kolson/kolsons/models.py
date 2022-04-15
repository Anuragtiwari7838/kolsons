from distutils.command.upload import upload
from django.db import models

# Create your models here. path("index/<int:id>",viewss.ind) , href="index/object.id"

class Product(models.Model):
    part_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=200,default="")
    images = models.ImageField(upload_to='document')
    Mounting_Style = models.CharField(max_length=200,blank=True,default="")
    Front_Protection = models.CharField(max_length=200,default="")
    Mounting_Cut_out = models.CharField(max_length=200,default="")
    Terminal = models.CharField(max_length=200,blank=True,default="Not Available")
    Front_Dimension = models.CharField(max_length=200,blank=True,default="Not Available")
    Operating_Voltage = models.CharField(max_length=200,blank=True,default="Not Available")
    Operating_Current = models.CharField(max_length=200,blank=True,default="Not Available")
    Lens_Colour = models.CharField(max_length=200,blank=True,default="Not Available")
    Lens_Shape = models.CharField(max_length=200,blank=True,default="Not Available")
    Lens_Material = models.CharField(max_length=200,blank=True,default="Not Available")
    Lens_Optics = models.CharField(max_length=200,blank=True,default="Not Available")
    Colour_Of_light = models.CharField(max_length=200,blank=True,default="Not Available")
    Front_Bezel_Colour = models.CharField(max_length=200,blank=True,default="Not Available")
    Front_Bezel_Material = models.CharField(max_length=200,blank=True,default="Not Available")
    Front_Ring_Colour = models.CharField(max_length=200,blank=True,default="Not Available")
    Front_Ring_Material = models.CharField(max_length=200,blank=True,default="Not Available")
    Contact = models.CharField(max_length=200,blank=True,default="Not Available")
    Contact_Material = models.CharField(max_length=200,blank=True,default="Not Available")
    Switching_Action = models.CharField(max_length=200,blank=True,default="Not Available")

    def __str__(self):
        return self.name