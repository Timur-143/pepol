from django.db import models

class Mod(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    text = models.TextField()
    category = models.ForeignKey(Mod, on_delete=models.CASCADE)