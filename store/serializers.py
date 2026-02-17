from decimal import Decimal
from store.models import Product, Collection, Promotion, Customer, Review, Cart, CartItem
from rest_framework import serializers



class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
        
    
        
        

    
    
class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    class Meta:
        model= Product
        fields = ['id', 'title', 'description', 'slug', 'unit_price', 'inventory',  'price_with_tax', 'collection']
        

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Promotion
        fields = ['id', 'description', 'discount']
    
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'membership' ]
        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']
        
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id= product_id, **validated_data)
    
class simpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']
    
class CartItemSerializer(serializers.ModelSerializer):
    product = simpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name = 'get_total_price')
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']
    
    def get_total_price(self, cart_Item: CartItem):
        
        return cart_Item.quantity * cart_Item.product.unit_price
    
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializer(many =True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    
    def get_total_price(self, cart: Cart):
        total = 0
        for item in cart.items.all():  # loops through each CartItem in the cart
            total += item.quantity * item.product.unit_price
        return total
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']
        
