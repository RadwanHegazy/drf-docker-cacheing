from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
import random

class ProductModel (models.Model) : 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='products-images/',null=True,blank=True)
    quantity = models.IntegerField()

    def __str__(self) : 
        return f'{self.title}'
    
    class Meta:
        ordering = ('-created_at',)
    
    def test () : 
        return ProductModel.objects.create(
            title = f'Product {random.randrange(1,100)}',
            description = f'Description For this product with random int ( {random.randrange(1,100)} )',
            price = random.randrange(1,1000),
            quantity = random.randrange(1,100),
            # image = open('C:\\Users\\ELsawah\\Desktop\\Me\\download.jpg','rb')
        )


class CartModel (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) : 
        return f"{self.user.username} ,{self.product} "


class Order (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    addresse = models.TextField(max_length=1000)
    isArrive = models.BooleanField(default=False)
    products = models.ManyToManyField(ProductModel, related_name='products_order')
    
    def __str__(self) :
        return f'{self.user.username} , {self.total_price} , Arrive : {self.isArrive}'




@receiver(post_save, sender = User)
def CreateUserToken (created, instance, **args) : 
    if created : 
        Token.objects.create( user = instance )


