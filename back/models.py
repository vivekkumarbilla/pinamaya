from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, DecimalField, IntegerField
from django.db.models.fields.files import ImageField

class Product(models.Model):
    CATEGORIES = (
        ('S','Scooter'),
        ('M','Motorcycle'),
        ('P','Moped'),
        ('E','Electric'),
        ('T','Three-Wheeler'),
    )
    name = CharField(max_length=100,verbose_name='Product Name')
    description = CharField(max_length=500,null=True,blank=True,verbose_name='Product Description')
    image = ImageField(null=True,blank=True,upload_to='images',verbose_name='Product Logo')
    # poster = ImageField(null=True,blank=True,upload_to='posters',verbose_name='Default Product Poster')
    model = CharField(max_length=100,verbose_name='Model Name')
    # exclusive = BooleanField(default=False,verbose_name='Mark as Exclusive')
    # category = CharField(max_length=50,choices=CATEGORIES, verbose_name='Product Category')
    size = DecimalField(max_digits=7, decimal_places=2,verbose_name='Size (in inches)',null=True,blank=True)
    frame = CharField(max_length=100,verbose_name='Frame')
    

    def __str__(self):
    	return self.name 
