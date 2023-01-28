from django.contrib import admin
from .models import User, Vendee, OrderItems, DeliveryOrder, Vendor

# Register your models here.
admin.site.register(User)
admin.site.register(Vendee)
admin.site.register(Vendor)
admin.site.register(OrderItems)
admin.site.register(DeliveryOrder)
