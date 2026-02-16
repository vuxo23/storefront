from decimal import Decimal
from store.models import Product, Collection, Promotion, Customer, Review, Cart, CartItem
from rest_framework import serializers



class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
        
    
        
        

    
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ['id', 'title', 'description', 'slug', 'unit_price', 'inventory',  'price_with_tax', 'collection']
        
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
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
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'created_at']
        

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'cart']
        