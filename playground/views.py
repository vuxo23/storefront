from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):

    return render(request, 'playground/hello.html', {'name': 'Vuxo'})


def firstapp(request):

    return render(request, 'playground/links.html')



