# sanghavi/models.py
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Place(models.Model):
    name = models.CharField(max_length=100)

class Driver(models.Model):
    name = models.CharField(max_length=100)

class Lorry(models.Model):
    number = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=100)

class UserInput(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    lorry = models.ForeignKey(Lorry, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_challan_no = models.CharField(max_length=20, blank=True)
    sales_challan_no = models.CharField(max_length=20, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    no_of_trips = models.IntegerField(blank=True, null=True)
    date1 = models.DateField(null=True, blank=True)
    date2 = models.DateField(null=True, blank=True)
    date3 = models.DateField(null=True, blank=True)
