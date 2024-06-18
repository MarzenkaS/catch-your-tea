from django.db import models


class ProductTestimonial(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(default=1)  # Rating from 1 to 5
    product = models.ForeignKey(ProductTestimonial, on_delete=models.CASCADE,
                                related_name='testimonials')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating} stars)"
