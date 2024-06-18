from django.shortcuts import render
from .models import Testimonial, ProductTestimonial
from .forms import TestimonialForm


def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonial_list.html',
                  {'testimonials': testimonials})
