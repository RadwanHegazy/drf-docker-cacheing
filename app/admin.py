from django.contrib import admin
from . import models
from . import AdminPanel
from django.contrib.auth.models import Group



# add models in admin
admin.site.register( models.ProductModel, AdminPanel.ProductAdminPanel )
admin.site.register( models.CartModel, AdminPanel.CartAdminPanel )
admin.site.register( models.Order, AdminPanel.OrderAdminPanel )

# remove model from admin
admin.site.unregister(Group)

