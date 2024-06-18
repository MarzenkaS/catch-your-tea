from django import forms
from .models import Testimonial
from products.models import Product


class TestimonialForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Choices from 1 to 5

    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rating')

    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'message', 'rating', 'product']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()
