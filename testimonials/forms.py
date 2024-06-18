from django import forms
from .models import Testimonial, ProductTestimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'message', 'rating', 'product']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'product': forms.Select(),
        }
