from django.db import models

class Product(models.Model):
    productName=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.FloatField()
    date_add=models.DateTimeField(auto_now_add=True)