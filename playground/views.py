from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from store.models import Product

# Create your views here.

def say_hello(request):
    # query_set=Product.objects.all()
    # query_set.filter()
    # for product in query_set:
    #     print(product)
    # return HttpResponse("Hello world")
    
    #lookup parameteres etc
    #none
    #filtering
    # query_set = Product.objects.all()
    # query_set=Product.objects.filter(Q(inventory__gt=10)|Q(unit_price__lt=10))
    #comparing fields
    products= Product.objects.order_by('title','unit_price')
    # product=Product.objects.earliest('title')
    # same_inventory_and_price=Product.objects.filter(inventory=F('unit_price'))
    return render(request, 'hello.html', {'name':"Furqan", 'products': list(products)})