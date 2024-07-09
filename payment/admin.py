from django.contrib import admin
from .models import ShippingAdress, Order, OrderItem

# Register the model on the admin section thing
admin.site.register(ShippingAdress)
admin.site.register(Order)
admin.site.register(OrderItem)
