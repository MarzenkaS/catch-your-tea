from django.contrib.auth.models import User
from django.db import models
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
    rating = models.IntegerField(default=1)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='testimonials'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Order by created_at in descending order

    def __str__(self):
        return f'Testimonial for {self.product.name}'

    def formatted_date(self):
        return self.created_at.strftime('%B %d, %Y')
