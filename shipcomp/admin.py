from django.contrib import admin
from .models import Item, Vendor, DistributionCenter, Shipments, ShippingDetails

admin.site.register(Item)
admin.site.register(Vendor)
admin.site.register(DistributionCenter)
admin.site.register(Shipments)
admin.site.register(ShippingDetails)


# Register your models here.
