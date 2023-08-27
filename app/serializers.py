from . import models
from rest_framework import serializers



class ProductSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = models.ProductModel
        fields = '__all__'


