from django.contrib import admin
from . import models
# Register your models here.

#modifying the product admin page
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','unit_price','inventory_status','collection_title']
    list_editable=['unit_price']
    list_per_page=10
    #this line is needed to avoid multiple sql queries
    list_select_related=['collection']
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory<50:
            return "Low"
        return "Normal"
    
    def collection_title(self,product):
        return product.collection.title

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'membership']
    list_editable=['membership']
    ordering=['first_name','last_name']
    list_per_page=10
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['payment_status', 'placed_at', 'customer_full_name']
    ordering=['placed_at']
    list_per_page=10
    list_select_related=['customer']

    def customer_full_name(self, order):
        return f"{order.customer.first_name} {order.customer.last_name}"


admin.site.register(models.Collection)

