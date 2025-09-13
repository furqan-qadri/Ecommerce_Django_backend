from urllib.parse import urlencode
from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html
from . import models
# Register your models here.

#modifying the product admin page
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions=["clear_inventory"]
    list_display=['title','unit_price','inventory_status','collection_title']
    list_editable=['unit_price']
    list_per_page=10
    list_filter=['last_update', 'collection']
    #this line is needed to avoid multiple sql queries
    list_select_related=['collection']
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory<50:
            return "Low"
        return "Normal"
    
    def collection_title(self,product):
        return product.collection.title
    
    @admin.action(description='Clear Inventory')
    def clear_inventory(self,request, queryset):
        updated_count=queryset.update(inventory=0)
        self.message_user(
            request,f'{updated_count} products successfully updated'
        )
        

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'membership']
    list_editable=['membership']
    ordering=['first_name','last_name']
    list_per_page=10
    search_fields=['first_name__istartswith', 'last_name__startswith']
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['payment_status', 'placed_at', 'customer_full_name']
    ordering=['placed_at']
    list_per_page=10
    list_select_related=['customer']

    def customer_full_name(self, order):
        return f"{order.customer.first_name} {order.customer.last_name}"


@admin.register(models.Collection)
class CollectionsAdmin(admin.ModelAdmin):
    list_display=['title','featured_product', 'products_count']
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url=(reverse('admin:store_product_changelist')+'?'+ urlencode({'collection__id': str(collection.id)}))
        return format_html('<a href="{}">{}</a>', url, collection)
        
    #It's like saying "Count how many products are connected to this collection while getting this"
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
        
