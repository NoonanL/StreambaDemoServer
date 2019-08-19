from django.db import models

# Create your models here.

#Custom User Model
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    profilePicture = models.ImageField(blank=True, null=True, upload_to='users/', max_length=255)

    def __str__(self):
        return self.username

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, null=True, related_name='tasks', on_delete=models.SET_NULL)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    status = models.CharField(max_length=128)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '%d: %s' % (self.id, self.title)


class Supplier(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    supplier = models.ForeignKey(Supplier, null=True, related_name='brands', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name




class Department(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, blank=True, default='')
    sku = models.CharField(max_length=128, unique=True)
    brand = models.ForeignKey(Brand, null=True, related_name='brand', on_delete=models.SET_NULL)
    mainImage = models.ImageField(blank=True, null=True, upload_to='products/', max_length=255)
    department = models.ForeignKey(Department, null=True, related_name='department', on_delete=models.SET_NULL)
    # productImages=models.ForeignKey(ProductImage, null=True, related_name='productImages', on_delete=models.SET_NULL)
    

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.sku



class ProductImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    imageName = models.CharField(max_length=128, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='products/', max_length=255)
    product = models.ForeignKey(Product, null=True, related_name='productImages', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.imageName


class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=128, blank=True, default='')
    surname = models.CharField(max_length=128)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '%d: %s' % (self.id, self.surname)

#a whole list of products tied to a customer
class Transaction(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    customer=models.ForeignKey(Customer, null=True, related_name='customer', on_delete=models.SET_NULL)
    product=models.ForeignKey(Product, related_name='product', on_delete=models.SET_DEFAULT, default=0)
    #list of products
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.id
