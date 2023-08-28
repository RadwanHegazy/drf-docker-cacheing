from django.urls import path
from . import views


urlpatterns = [

    # Products
    path('',views.Products.as_view()),
    
    # View product details
    path('<int:pk>/',views.ProductDetails.as_view()),

    # cart [ add and view ]
    path('cart/',views.Cart.as_view()),

    
    # order [ view and confirm ]
    path('order/',views.Order.as_view()),
]