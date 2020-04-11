from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Products.objects.all()
