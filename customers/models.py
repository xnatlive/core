from django.db import models


# Create your models here.
class Company(models.Model):
    name= models.CharField(max_length =40)
    nID = models.CharField(max_length =12)
    ceoName = models.CharField(max_length =40,null=True)
    career = models.CharField(max_length =40)
    mobile = models.CharField(max_length =12)
    tel =models.CharField(max_length =12,null=True)
    address =models.TextField(null=True)
    note = models.TextField(null=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name= models.CharField(max_length =40)
    family= models.CharField(max_length =40)
    nID = models.CharField(max_length =12)
    career = models.CharField(max_length =40)
    mobile = models.CharField(max_length =12)
    tel =models.CharField(max_length =12,null=True)
    address =models.TextField(null=True)
    note = models.TextField(null=True)
    def __str__(self):
        return self.name
    
