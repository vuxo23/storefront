from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator
from uuid import uuid4
from django.conf import settings
from rest_framework import permissions
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title= models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null= True, related_name='+' )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

        



class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(default="-")
    description = models.TextField(null = True, blank=True)
    unit_price = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(1)]
        )
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')
    promotions = models.ManyToManyField(Promotion, blank = True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

class Customer(models.Model):
    MEMBERSHIP_Bronze = 'B'
    MEMBERSHIP_Gold = 'G'
    MEMBERSHIP_Silver = 'S'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_Bronze, 'Bronze'),
        (MEMBERSHIP_Gold, 'Gold'),
        (MEMBERSHIP_Silver, 'Sliver')
    ]
    phone = models.CharField(max_length= 255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_Bronze)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    class Meta:
        ordering = ['user__first_name' , 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]

class Order(models.Model):
    PAYMENT_Pending = 'P'
    PAYMENT_Complete = 'C'
    PAYMENT_Failed = 'F'

    PAYMENT_STATUS= [
        (PAYMENT_Pending, 'Pending'),
        (PAYMENT_Complete, 'Complete'),
        (PAYMENT_Failed, 'Failed')
    ]

    payment = models.CharField(max_length=1,choices= PAYMENT_STATUS, default= PAYMENT_Pending )
    place_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    class Meta:
        permissions = [
            ('cancel_order', 'can cancel order')
        ]
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='OrderItem')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    
    
    

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at= models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items') 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
        )
    class Meta:
        unique_together = [['cart', 'product']]

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
class Review(models.Model):
    product =models.ForeignKey(Product, on_delete= models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    
    
    

    

