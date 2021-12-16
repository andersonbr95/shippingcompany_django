from django.db import models


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=25)
    main_contact = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.vendor_name

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name

class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.warehouse_name


class DistributionCenter(models.Model):
    dist_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.dist_name

class Shipments(models.Model):
    dist_center = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
    departure_date = models.DateTimeField
    expected_arrival_date = models.DateTimeField
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    received = models.BooleanField()
    #shipping_weight = models.PositiveIntegerField(default=0)
    shipping_weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.expected_arrival_date
    def __bool__(self):
        return self.received



class ShippingDetails(models.Model):
    shipment = models.ForeignKey(Shipments, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(4)

    def __int__(self):
        return self.quantity




# Create your models here.
