from django.db import models
from avodhashopapp.models import Product


class Cart(models.Model):
    def __str__(self):
        return self.cart_id

    cart_id = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    def __str__(self):
        return self.prodt

    prodt = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def total(self):
        return self.prodt.price * self.quantity







