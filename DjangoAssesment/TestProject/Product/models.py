from django.db import models


# Create your models here.

class ProductMainModel(models.Model):
    unique_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()


class ImageModel(models.Model):
    product_id = models.IntegerField()
    image = models.CharField(max_length=200)


class CartModel(models.Model):
    owner = models.IntegerField()
    products = models.IntegerField()
    price = models.IntegerField()


class TestClass(models.Model):
    my_image = models.ImageField(upload_to="Images")


