from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, DecimalField, IntegerField
from django.db.models.fields.files import ImageField
from colorfield.fields import ColorField
from django.db.models.fields.related import ForeignKey, ManyToManyField

class Product(models.Model):
    model = CharField(max_length=100,verbose_name='Model')
    description = CharField(max_length=500,null=True,blank=True,verbose_name='Product Description')
    image = ImageField(null=True,blank=True,upload_to='products',verbose_name='Product Image')
    # size = DecimalField(max_digits=4, decimal_places=2,verbose_name='Size (in inches)')
    price = IntegerField(max_length=100,verbose_name='Price in Rupees',null=True,blank=True)
    frame = CharField(max_length=100,verbose_name='Frame',null=True,blank=True)
    fork = CharField(max_length=50,null=True,blank=True,verbose_name='Fork')
    decal = CharField(max_length=70,null=True,blank=True,verbose_name='Decal')
    chain = CharField(max_length=70,null=True,blank=True,verbose_name='Chain')
    pedal = CharField(max_length=70,null=True,blank=True,verbose_name='Pedal')
    bottombracket = CharField(max_length=70,null=True,blank=True,verbose_name='Bottom Bracket')
    fderaileur = CharField(max_length=70,null=True,blank=True,verbose_name='Front Deraileur')
    rderaileur = CharField(max_length=70,null=True,blank=True,verbose_name='Rear Deraileur')
    shifter = CharField(max_length=70,null=True,blank=True,verbose_name='Shifter')
    rims = CharField(max_length=70,null=True,blank=True,verbose_name='Rims')
    tyre = CharField(max_length=70,null=True,blank=True,verbose_name='Tyre')
    tube = CharField(max_length=70,null=True,blank=True,verbose_name='Tube')
    headset = CharField(max_length=70,null=True,blank=True,verbose_name='Headset')
    handlebar = CharField(max_length=70,null=True,blank=True,verbose_name='Handle Bar')
    stem = CharField(max_length=70,null=True,blank=True,verbose_name='Stem')
    saddle = CharField(max_length=70,null=True,blank=True,verbose_name='Saddle')
    amazonlink = CharField(max_length=300,null=True,blank=True,verbose_name='Amazon Link')

    def __str__(self):
    	return self.model

        
class Image(models.Model):
    title = CharField(max_length=100,verbose_name='Image/Event Title')
    description = CharField(max_length=500,null=True,blank=True,verbose_name='Description of the Event/Image')
    image = ImageField(null=True,blank=True,upload_to='images',verbose_name='Main Image')
    def __str__(self):
    	return 'Image: ' + self.title

class Color(models.Model):
    of = ForeignKey(Product, on_delete=models.CASCADE,null=True)
    colorname = CharField(max_length=50,verbose_name='Color Variant Name')
    color = ColorField(default='#ffffff',format='hexa')
    image = ImageField(null=True,blank=True,upload_to='colors',verbose_name='Color Variant Image')
    def __str__(self):
        return self.colorname

class Size(models.Model):
    of = ForeignKey(Product, on_delete=models.CASCADE,null=True)
    size = DecimalField(max_digits=4, decimal_places=2,verbose_name='Size (in inches)')
    def __str__(self):
        return str(self.size)

class Event(models.Model):
    title = CharField(max_length=50,verbose_name='Title of Event')
    description = CharField(max_length=500,verbose_name='Event Description',null=True)
    url = CharField(max_length=100,verbose_name='Link of Event',null=True)
    image = ImageField(null=True,blank=True,upload_to='events',verbose_name='Event Image')

    

class Email(models.Model):
    email = CharField(max_length=50,verbose_name='Email of a User')

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            print('sending email')
        super(Email, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
    

