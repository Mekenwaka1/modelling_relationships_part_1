from django.db import models

class Customer(models.Model):
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

class Order(models.Model):
    order_number = models.IntegerField()
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
