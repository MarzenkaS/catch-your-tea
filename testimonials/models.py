from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product


class ProductTestimonial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='testimonials'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Testimonial for {self.product.name}'
