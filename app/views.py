from rest_framework import generics, filters, status ,permissions, authentication, mixins
from . import serializers
from . import models
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework import pagination



class Products (generics.GenericAPIView, mixins.ListModelMixin) : 
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    

    def get (self, request) : 
        
        if cache.get('products') :
            products = cache.get('products')
            serializer = self.serializer_class(products, many=True)
            return self.list(serializer.data)

        else :
            cache.set('products',models.ProductModel.objects.all())
            return self.list(request)



    def paginate_queryset(self,queryset):

        if 'page' in self.request.GET : 
            page_name = f'page={self.request.GET["page"]}'
            
            if cache.get(page_name) is not None: 
                products = cache.get(page_name)
                return super().paginate_queryset(queryset=products) 
            else :
                cache.set(page_name,queryset)
                return super().paginate_queryset(queryset) 
        else :
            page_name = 'page=0'

            if cache.get(page_name) is not None: 
                return super().paginate_queryset(queryset=cache.get(page_name))
            else : 
                cache.set(page_name,queryset)
                return super().paginate_queryset(queryset=queryset)
            
    
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

