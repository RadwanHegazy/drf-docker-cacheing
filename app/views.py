from django.shortcuts import render, HttpResponse
from rest_framework import decorators, generics, filters, permissions, authentication, mixins
from . import serializers
from . import models
from rest_framework.response import Response

class Products (generics.GenericAPIView, mixins.ListModelMixin) : 
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    

    def get (self, request) : 
        return self.list(request)

class ProductDetails (generics.GenericAPIView, mixins.RetrieveModelMixin) : 
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]

    def get(self, request, **kwargs) : 
        return self.retrieve(request)



def wishlist (request) :
    return HttpResponse('Done') 


def order (request) :
    return HttpResponse('Done') 




