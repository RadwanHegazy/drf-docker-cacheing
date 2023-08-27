from django.contrib import admin
from . import models


class ProductAdminPanel (admin.ModelAdmin) : 
    list_display = ['title','price','created_at']
    search_fields = ['title']


class CartAdminPanel (admin.ModelAdmin) :
    list_display = ['user','product','quantity']
    search_fields = ['user']

class OrderAdminPanel (admin.ModelAdmin) : 
    list_display = ['user','total_price','isArrive']