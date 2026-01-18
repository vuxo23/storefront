from django.urls import path
from . import views

urlpatterns = [
    path('fifo/', views.firstapp),
    path('hello/', views.say_hello)
    
]
