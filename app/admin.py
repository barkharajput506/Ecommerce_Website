from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (Customer, Product, Cart, OrderPlaced)

@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']    

@admin.register(OrderPlaced)
class AdminOrderPlaced(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info', 'quantity', 'ordered_date', 'status']    

    
    # to generate link in database for customer information
    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
    
    # to generate link in database for product details
    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)