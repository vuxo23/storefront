from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product, Collection, OrderItem, Review, Promotion, Customer,Cart
from .serializers import *;
from .filters import ProductFilter
from .pagination import DefaultPagination



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    pagination_class = DefaultPagination

    
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id= kwargs['pk']).count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        return super().destroy(request, *args, **kwargs)

            
class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    

    
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id = kwargs['pk']).count() >0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products'}, status= status.HTTP_405_METHOD_NOT_ALLOWED)
    
        return super().destroy(request, *args, **kwargs)
    
    
class PromotionsViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    
    
class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(product_id= self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    
class CartViewSet(ModelViewSet):
    serializer_class = CartItem
    def get_queryset(self):
        return Cart.objects.filter(cartItem_id= self.kwargs['cartItem_pk'])
    
    def get_serializer_context(self):
        return {'cartItem_id': self.kwargs['cartItem_pk']}
    
class CartItemViewSet(ModelViewSet):
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
    
    
