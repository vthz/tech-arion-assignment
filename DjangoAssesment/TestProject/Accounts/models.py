from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField()
    is_customer = models.BooleanField()
    is_admin = models.BooleanField()


class userProfileModel(models.Model):
    owner = models.IntegerField()
    name = models.CharField(max_length=30)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=10)
    image = models.ImageField()


class loginTopModel(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.IntegerField()
    otp = models.IntegerField()
    active = models.BooleanField()


class userCartProductModel(models.Model):
    owner = models.IntegerField()
    products = models.IntegerField()
    price = models.IntegerField()


class CartModel(models.Model):
    owner = models.IntegerField()
    products = models.IntegerField()
    price = models.IntegerField()
