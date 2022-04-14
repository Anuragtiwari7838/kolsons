from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Product(models.Model):
    part_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=2000)
    images = models.ImageField(upload_to='document')
    pdf = models.FileField(upload_to='document')

    def __str__(self):
        return self.name