from django.shortcuts import render, HttpResponse
from rest_framework import decorators, generics, filters, status ,permissions, authentication, mixins
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




class Cart (generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin) :
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerailizer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get (self, request) : 
        user = request.user
        user_carts = models.CartModel.objects.filter( user = user )

        serailizer = self.serializer_class(user_carts, many=True)

        return Response( serailizer.data , status=status.HTTP_200_OK )
    
    
    def post (self, request) : 
        return self.create(request)



class Order (generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin) :
    queryset = models.Order
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get ( self, request ) : 

        user = request.user

        self.orders = models.Order.objects.filter( user = user )
        serializer = serializers.OrderSerializer( self.orders , many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


    def post (self, request) : 

        user = request.user
        addresse = request.POST['addresse']
        
        user_cart = models.CartModel.objects.filter( user = user )
        total_price = sum([( i.product.price * i.quantity ) for i in user_cart])

        order = models.Order.objects.create(
            user = user,
            addresse = addresse,
            total_price = total_price,
        )

        
        for cart in user_cart :order.products.add(cart.product)

        order.save()
        

        serializer = serializers.OrderSerializer(order)

        return Response( serializer.data, status=status.HTTP_201_CREATED )

