from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM store_product")
        
    return render(request, 'playground/hello.html', {'name': 'Vuxo', 'products': products})


def firstapp(request):
    return render(request, 'playground/links.html')



