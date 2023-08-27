from django.urls import path
from . import views


urlpatterns = [
    path('',views.Products.as_view()),
    path('<int:pk>/',views.ProductDetails.as_view())
]