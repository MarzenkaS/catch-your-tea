from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Wishlist
from products.models import Product
from django.contrib import messages


def wishlist_view(request):
    wishlist = Wishlist.objects.get(user=request.user)
    teas = wishlist.products.all()
    context = {
        'teas': teas,
    }
    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, product_id):
    if not request.user.is_authenticated:
        messages.info(request, "You need to log in or register to add products to your wishlist.")
        return redirect('login')  # Redirect to your login page

    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the wishlist
    if product in wishlist.teas.all():
        messages.info(request, f"{product.name} is already in your wishlist.")
    else:
        wishlist.teas.add(product)
        messages.success(request, f"{product.name} has been added to your wishlist.")

    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    tea = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if tea in wishlist.teas.all():
        wishlist.teas.remove(tea)
        return redirect('wishlist')
    else:
        return HttpResponseForbidden("You do not have permission to remove this item from your wishlist.")
