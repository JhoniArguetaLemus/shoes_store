from django.db import models


class Product(models.Model):
    productname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField()
    date_add = models.DateTimeField(auto_now_add=True)
 


class Men(models.Model):
    shoe_name = models.CharField(max_length=100)
    shoe_description = models.CharField(max_length=100)
    shoe_price = models.FloatField()
    shoes_tock = models.IntegerField()
    image_url=models.URLField( null=True, blank=False )


class Childs(models.Model):
    shoe_name = models.CharField(max_length=100)
    shoe_description = models.CharField(max_length=100)
    shoe_price = models.FloatField()
    shoe_stock = models.IntegerField()
    image_url=models.URLField( null=True, blank=False )

class Woman(models.Model):
    shoe_name = models.CharField(max_length=100)
    shoe_description = models.CharField(max_length=100)
    shoe_price = models.FloatField()
    shoe_stock = models.IntegerField()
    image_url=models.URLField( null=True, blank=False )
