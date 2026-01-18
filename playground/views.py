from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    x = 1
    y = 2
    query_set = Product.objects.all()
    for product in query_set:
        print(product)
   
    return render(request, 'playground/hello.html', {'name': 'Vuxo'})


def firstapp(request):

    return render(request, 'playground/links.html')



