from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin;
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView;
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Collection
from django.db.models import Count
from .serializers import ProductSerializer, CollectionSerializer

ProductSerializer()
CollectionSerializer()

class ProductList(ListCreateAPIView):
    
    queryset= Product.objects.select_related('collection').all()
    
    serializer_class  = ProductSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk) 
        if product.OrderItem.count() >0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(products_count = Count('products')).all()
    serializer_class = CollectionSerializer
    
    
@api_view(['GET', 'PUT','DELETE'])
def collection_detail(request, id):
    collection = get_object_or_404(Collection.objects.annotate(products_count= Count('products')), pk = id)
    
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if collection.products.count()> 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products'})
        
        collection.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
