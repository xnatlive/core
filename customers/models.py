from django.db import models
from django.forms import ModelForm



# Create your models here.
class Company(models.Model):
    name= models.CharField(max_length =40)
    nID = models.CharField(max_length =12)
    ceoName = models.CharField(max_length =40)
    career = models.CharField(max_length =40)
    mobile = models.CharField(max_length =12)
    tel =models.CharField(max_length =12)
    address =models.TextField()
    note = models.TextField()
    def __str__(self):
        return self.name

class Customer(models.Model):
    name= models.CharField(max_length =40)
    nID = models.CharField(max_length =12)
    career = models.CharField(max_length =40)
    mobile = models.CharField(max_length =12)
    tel =models.CharField(max_length =12)
    address =models.TextField()
    note = models.TextField()
    def __str__(self):
        return self.name
    

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields =['name','nID','ceoName','career','mobile', 'tel','address','note']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields =['name','nID','career','mobile', 'tel','address','note']