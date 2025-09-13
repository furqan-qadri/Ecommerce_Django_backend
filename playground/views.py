from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F, Value
from store.models import Product, Customer

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
    # products= Product.objects.order_by('title','unit_price')
    # products=Product.objects.values('title','unit_price')
    # product=Product.objects.earliest('title')
    # same_inventory_and_price=Product.objects.filter(inventory=F('unit_price'))
    
    
    #selecting related objects
    #selected_related(1)
    #prefetch_related(n)
    # products=Product.objects.select_related('collection').all()
    #  products=Product.objects.select_related('collection').all()
    #  can also combine both since both return a queryset
    # products=Product.objects.select_related('collection').prefetch_related('promotions')
    
    
    #aggregate fields
    # query_set=Customer.objects.annotate(is_new=Value(True))
    
    #setting new id= old id+1
    query_set=Customer.objects.annotate(new_id=F('id')+1)
    
    return render(request, 'hello.html', {'name':"Furqan", 'customers': query_set})