from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class BagItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} ({self.user.username})"
