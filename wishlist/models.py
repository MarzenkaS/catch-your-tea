from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# class Tea(models.Model):
    # name = models.CharField(max_length=100)
    # description = models.TextField()
    # amount_in_gram = models.IntegerField(null=True, blank=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Wishlist for {self.user.username}"
