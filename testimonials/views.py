from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Testimonial
from .forms import TestimonialForm
from products.models import Product


def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})


@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product'].id
            if Product.objects.filter(id=product_id).exists():
                testimonial = form.save(commit=False)
                testimonial.user = request.user
                testimonial.save()
                return redirect('testimonials:testimonial_list')
            else:
                pass
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/add_testimonial.html', {'form': form})


@login_required
def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonials:testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'testimonials/edit_testimonial.html', {'form': form})


@login_required
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonials:testimonial_list')
    return render(request, 'testimonials/delete_testimonial.html', {'testimonial': testimonial})
