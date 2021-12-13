from django.db import models


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50),
    city = models.CharField(max_length=50),
    state = models.CharField(max_length=2),
    country = models.CharField(max_length=25),
    main_contact = models.CharField(50),
    phone_number = models.CharField(max_length=15)

class Item(models.Model):
    item_name = models.CharField(max_length=50),
    unit_price = models.IntegerField(5),
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE),
    item_description = models.CharField(max_length=100)

class Warehouse(models.Model):
    address = models.CharField(max_length=50),
    city = models.CharField(max_length=50),
    state = models.CharField(max_length=2)

class DistributionCenter(models.Model):
    address = models.CharField(max_length=50),
    city = models.CharField(max_length=50),
    state = models.CharField(max_length=2)

class Shipments(models.Model):
    dist_center = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE),
    departure_date = models.DateTimeField,
    expected_arrival_date = models.DateTimeField,
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE),
    received = models.BooleanField(),
    shipping_weight = models.IntegerField()

class ShippingDetails(models.Model):
    shipment = models.ForeignKey(Shipments, on_delete=models.CASCADE),
    item = models.ForeignKey(Item, on_delete=models.CASCADE),
    quantity = models.IntegerField(4)




# Create your models here.
