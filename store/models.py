from enum import unique
from tkinter import CASCADE
from django.db import models
from django.db.models import indexes

# Create your models here.

class Promotion(models.Model):
    description=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    discount=models.FloatField()
    
    
class Collection(models.Model):
    title=models.CharField(max_length=255)
    featured_product=models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    
class Product(models.Model):
    sku=models.CharField(max_length=15)
    title= models.CharField(max_length=255)
    description=models.TextField()
    slug=models.SlugField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion)
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    #human readable forms
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)
    # class Meta:
    #     db_table="store_customers" #change the name of the table
    #     indexes=[models.Index(fields=['first_name','last_name'])] 
        
    
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED='F'
    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed')
    ]
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    placed_at=models.DateField(auto_now_add=True)
    customer=models.ForeignKey(Customer, on_delete=models.PROTECT)
    

#one to one relationship
class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    # if one-one relationship
    # customer=models.OneToOneField(Customer, on_delete=CASCADE, primary_key=True)
    #cascade deletes the address if the parent i.e the customer is deleted.
    
    # if one to many i.e customer has more than one addresses
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)

