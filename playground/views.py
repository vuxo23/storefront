from django.shortcuts import render
#from django.http import HttpResponse

def firstapp(request):
    x = 1
    y = 2
    return render(request, 'playground/links.html')

