from . import models
from rest_framework import serializers



class ProductSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = models.ProductModel
        fields = '__all__'



class CartSerailizer ( serializers.ModelSerializer ) : 
    class Meta : 
        model = models.CartModel
        fields = "__all__"

        
