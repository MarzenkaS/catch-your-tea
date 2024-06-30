from django.db import models
from django.contrib.auth.models import User


class Tea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teas = models.ManyToManyField(Tea)

    def __str__(self):
        return f"Wishlist of {self.user.username}"
