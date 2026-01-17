from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title= models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null= True, related_name='+' )


class Product(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places= 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_Bronze = 'B'
    MEMBERSHIP_Gold = 'G'
    MEMBERSHIP_Silver = 'S'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_Bronze, 'Bronze'),
        (MEMBERSHIP_Gold, 'Gold'),
        (MEMBERSHIP_Silver, 'Sliver')
    ]
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length= 255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_Bronze)

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

class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Cart(models.Model):
    created_at= models.DateTimeField(auto_now=True)
    quantity = models.PositiveSmallIntegerField()

class CartItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

     

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    
    
    

    

