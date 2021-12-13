from django.db import models


class Vendor(models.Model):
    vendor_name = models.CharField(50),
    city = models.CharField(50),
    state = models.CharField(2),
    country = models.CharField(25),
    main_contact = models.CharField(50),
    phone_number = models.CharField(15)

class Item(models.Model):
    item_name = models.CharField(50),
    unit_price = models.IntegerField(5),
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE),
    item_description = models.CharField(100)

class Warehouse(models.Model):
    address = models.CharField(50),
    city = models.CharField(50),
    state = models.CharField(2)

class DistributionCenter(models.Model):
    address = models.CharField(50),
    city = models.CharField(50),
    state = models.CharField(2)

class Shipments(models.Model):
    dist_center_id = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE),
    departure_date = models.DateTimeField,
    expected_arrival_date = models.DateTimeField,
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE),
    received = models.BooleanField(),
    shipping_weight = models.IntegerField()

class ShippingDetails(models.Model):
    shipment_id = models.ForeignKey(Shipments, on_delete=models.CASCADE),
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE),
    quantity = models.IntegerField(4)




# Create your models here.
